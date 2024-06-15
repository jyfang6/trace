import os
import time 
import argparse
import numpy as np
from copy import deepcopy
from tqdm import tqdm
from typing import List, Dict

import torch 
from torch import Tensor
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForCausalLM 
from transformers import logging as hf_logging
hf_logging.set_verbosity_error()

from utils.utils import * 
from utils.const import HF_TOKEN 
from retrievers.e5_mistral import get_e5_mistral_embeddings_for_query, get_e5_mistral_embeddings_for_document
from retrievers.dragon_plus import get_dragon_plus_embeddings_for_query, get_dragon_plus_embeddings_for_document
from retrievers.e5 import get_e5_embeddings_for_query, get_e5_embeddings_for_document


tokenizer = None 
model = None 
token_id_to_choice_map = None
choices_token_ids_list = None

tokenizer_name_or_path = "meta-llama/Meta-Llama-3-8B-Instruct"
model_name_or_path = "meta-llama/Meta-Llama-3-8B-Instruct"
device = torch.device("cuda")


def setup_parser():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset", type=str, default="hotpotqa")
    parser.add_argument("--input_data_file", type=str, default="data/hotpotqa/dev_with_kgs.json")
    parser.add_argument("--save_data_file", type=str, default="data/hotpotqa/dev_with_reasoning_chains.json")

    parser.add_argument("--ranking_model", type=str, default="e5_mistral")
    parser.add_argument("--max_chain_length", type=int, default=4)
    parser.add_argument("--num_choices", type=int, default=20)
    parser.add_argument("--num_examplars", type=int, default=3)
    parser.add_argument("--max_length", type=int, default=2048)
    parser.add_argument("--max_new_tokens", type=int, default=16)
    parser.add_argument("--num_beams", type=int, default=5)
    parser.add_argument("--num_chains", type=int, default=20)
    parser.add_argument("--min_triple_prob", type=float, default=1e-4)
    parser.add_argument("--disable_demonstration", action="store_true")
    parser.add_argument("--calculate_ranked_prompt_indices", action="store_true", help="whether to use retriever to adaptively choose demonstrations")

    args = parser.parse_args()
    return args


def get_tokenizer():
    padding_side = "left"
    print(f"loading tokenizer for \"{tokenizer_name_or_path}\" with padding_side: \"{padding_side}\"")
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, padding_side=padding_side, token=HF_TOKEN)
    if tokenizer.pad_token is None or tokenizer.pad_token_id is None:
        print("Missing padding token, setting padding token to eos_token")
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    return tokenizer


def get_model():
    print(f"loading {model_name_or_path} model in bfloat16 ...")
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path, torch_dtype=torch.bfloat16, token=HF_TOKEN)
    model.to(device)
    model.eval()
    return model 


def get_dataset_demonstrations(dataset):

    if dataset == "hotpotqa":
        from prompts import generate_reasoning_chains_hotpotqa_examplars, reasoning_chains_hotpotqa_examplars
        return generate_reasoning_chains_hotpotqa_examplars, reasoning_chains_hotpotqa_examplars
    elif dataset == "2wikimultihopqa":
        from prompts import generate_reasoning_chains_2wikimultihopqa_examplars, reasoning_chains_2wikimultihopqa_examplars
        return generate_reasoning_chains_2wikimultihopqa_examplars, reasoning_chains_2wikimultihopqa_examplars
    elif dataset == "musique":
        from prompts import generate_reasoning_chains_musique_examplars, reasoning_chains_musique_examplars
        return generate_reasoning_chains_musique_examplars, reasoning_chains_musique_examplars
    else:
        raise ValueError(f"{dataset} is not a supported dataset!")


def get_llama3_generate_reasoning_chains_prompts_chat_format(
    args, 
    hop: int, 
    question: str, 
    existing_triples: List[List[str]], 
    candidate_triples: List[List[str]],
    ranked_prompt_indices: list = None, 
) -> List[str]:

    global tokenizer
    tokenizer = get_tokenizer() if tokenizer is None else tokenizer

    def convert_candidate_triples_to_choices(candidates): 
        return "\n".join(["A. no need for additional knowledge triples"] \
            + ["{}. {}".format(chr(ord('B')+k), triple) for k, triple in enumerate(candidates)])

    def convert_several_examplars_to_text(examplars):
        return "\n\n".join(examplars)
    
    def vary_num_examplars_based_on_context_window(instruction, examplars, question, triples, candidates):
        final_examplars = None
        while len(examplars) > 0:
            for num in range(len(examplars), 0, -1):
                possible_prompt = "{} {}\n\nquestion: {}\nknowledge triples: {}\ncandidate knowledge triples:\n{}\nanswer:".format(
                    instruction, convert_several_examplars_to_text(examplars[:num]), 
                    question, " ".join(triples), convert_candidate_triples_to_choices(candidates)
                )
                possible_prompt_tokens = tokenizer.encode(possible_prompt)
                if len(possible_prompt_tokens) <= args.max_length:
                    final_examplars = examplars[:num]
                    break
            if final_examplars is None:
                examplars = examplars[1:]
            else:
                break
        if final_examplars is None:
            final_examplars = [] 
        return final_examplars

    prompts = []
    for triples, candidates in zip(existing_triples, candidate_triples):

        instruction = "Select the next knowledge triple that extends an existing set of knowledge triples to form a coherent reasoning chain capable of answering a specified question. " \
            "If the current reasoning chain is sufficient to answer the question, simply output A. Please only output the choice for the next knowledge triple."
        
        if not args.disable_demonstration:
            instruction += "\n\nThe followings are some examples of coherent reasoning chains capable of answering the specified question " \
                f"and how the {hop+1}-th knowledge triples in these chains are selected:\n\n"
            generate_reasoning_chains_examplars, reasoning_chains_examplars = get_dataset_demonstrations(args.dataset)
            if ranked_prompt_indices is not None:
                reasoning_chains_examplars = [reasoning_chains_examplars[idx] for idx in ranked_prompt_indices]
                generate_reasoning_chains_examplars = [generate_reasoning_chains_examplars[idx] for idx in ranked_prompt_indices]

            examplars = [] 
            for i, (rp_examplar, grp_examplar) in enumerate(
                zip(
                    reasoning_chains_examplars, 
                    generate_reasoning_chains_examplars
                )
            ):
                if len(grp_examplar) < hop + 1:
                    continue 
                examplar = "coherent reasoning chain: {}\nquestion: {}\n".format(rp_examplar["chains"], rp_examplar["question"])
                examplar += "The {}-th triple in the reasoning chain is selected as:\n".format(hop+1)
                one_step_item = grp_examplar[hop]
                examplar += "existing knowledge triples: {}\nquestion: {}\ncandidate knowledge triples:\n{}\nthe next possible triple is:{}\n".format(
                    ", ".join(one_step_item["triples"]), one_step_item["question"], "\n".join(one_step_item["candidate_triples"]), one_step_item["answer"]
                )
                examplars.append(examplar)
                if len(examplars) >= args.num_examplars:
                    break 
            examplars = vary_num_examplars_based_on_context_window(instruction, examplars, question, triples, candidates)
            instruction += convert_several_examplars_to_text(examplars)
        else:
            instruction += "\n\n"
        
        user_input_text = "The {}-th triple in the reasoning chain is selected as:\nexisting knowledge triples: {}\nquestion: {}\ncandidate knowledge triples:\n{}\nthe next possible triple is:".format(
            hop+1, ", ".join(triples), question, convert_candidate_triples_to_choices(candidates)
        )
        prompts.append(
            [
                {"role": "system", "content": instruction}, 
                {"role": "user", "content": user_input_text}
            ]
        )
    
    return prompts


def tokenizer_encode_chat_format_for_instruction_model(prompts: List[List[dict]], max_length: int=4096) -> Dict[str, Tensor]:

    global tokenizer 
    tokenizer = get_tokenizer() if tokenizer is None else tokenizer 
    
    texts = tokenizer.apply_chat_template(prompts, tokenize=False, add_generation_prompt=True)
    batch_dict = tokenizer(texts, max_length=max_length, padding=True, truncation=True, return_tensors='pt')
    tokenizer_outputs = {"input_ids": batch_dict["input_ids"], "attention_mask": batch_dict["attention_mask"]}

    return tokenizer_outputs 


def model_generate(inputs: Dict[str, Tensor], max_new_tokens: int=100, batch_size=2) -> Tensor:

    global tokenizer, model 
    model = get_model() if model is None else model 
    generated_token_ids_list, generated_token_logits_list = [], [] 
    for i in range((len(inputs["input_ids"])-1)//batch_size+1):
        batch_inputs = {k: v[i*batch_size: (i+1)*batch_size] for k, v in inputs.items()}
        batch_inputs = to_device(batch_inputs, device)
        batch_outputs = model.generate(**batch_inputs, max_new_tokens=max_new_tokens, output_scores=True, return_dict_in_generate=True, do_sample=False, temperature=1.0) # temperature=1.5, do_sample=True) # 
        batch_generated_token_ids = batch_outputs.sequences[:, batch_inputs["input_ids"].shape[1]:].detach().cpu()
        batch_generated_token_logits = torch.cat([token_scores.unsqueeze(1) for token_scores in batch_outputs.scores], dim=1).detach().cpu()

        if batch_generated_token_ids.shape[1] < max_new_tokens:
            real_batch_size, num_generated_tokens = batch_generated_token_ids.shape 
            padding_length = max_new_tokens-num_generated_tokens
            padding_token_ids = torch.zeros((real_batch_size, padding_length), dtype=batch_generated_token_ids.dtype).fill_(tokenizer.pad_token_id)
            padding_token_logits = torch.zeros((real_batch_size, padding_length, batch_generated_token_logits.shape[-1]), dtype=batch_generated_token_logits.dtype)
            batch_generated_token_ids = torch.cat([batch_generated_token_ids, padding_token_ids], dim=1)
            batch_generated_token_logits = torch.cat([batch_generated_token_logits, padding_token_logits], dim=1)
        
        generated_token_ids_list.append(batch_generated_token_ids)
        generated_token_logits_list.append(batch_generated_token_logits)

    generated_token_ids = torch.cat(generated_token_ids_list, dim=0)
    generated_token_logits = torch.cat(generated_token_logits_list, dim=0)

    return generated_token_ids, generated_token_logits


def get_answer_token_indices(num_choices, token_ids):

    global tokenizer, token_id_to_choice_map 
    if token_id_to_choice_map is None:
        token_id_to_choice_map = {}
        choices = [chr(ord('A')+i) for i in range(num_choices+1)] 
        for choice in choices:
            token_id_to_choice_map[tokenizer.encode(choice, add_special_tokens=False)[0]] = choice
            token_id_to_choice_map[tokenizer.encode(" {}".format(choice), add_special_tokens=False)[-1]] = choice
    
    answer_token_indices = torch.zeros((token_ids.shape[0],), dtype=token_ids.dtype).fill_(token_ids.shape[1]-1)
    for i in range(token_ids.shape[0]):
        for j in range(token_ids.shape[1]):
            if token_ids[i, j].item() in token_id_to_choice_map:
                answer_token_indices[i] = j 
                break

    return answer_token_indices


def construct_reasoning_chains(args):

    data_file, save_data_file = args.input_data_file, args.save_data_file 

    if os.path.exists(save_data_file):
        print(f"{save_data_file} already exists, skip this ...")
        return
    
    print(f"loading data from {data_file} ... ")
    data = load_json(data_file)
    
    if args.calculate_ranked_prompt_indices:
        _, reasoning_chains_examplars = get_dataset_demonstrations(args.dataset)
        questions_in_examplars = [item["question"] for item in reasoning_chains_examplars]
        questions_in_data = [item["question"] for item in data]
        if args.ranking_model == "e5_mistral":
            print("Calculating E5-Mistral Embeddings of Questions in Prompts ... ")
            questions_in_prompts_embeddings = get_e5_mistral_embeddings_for_document(questions_in_examplars, max_length=128, batch_size=2)
            print("Calculating E5-Mistral Embeddings of Questions in Data ... ")
            questions_in_data_embeddings = get_e5_mistral_embeddings_for_document(questions_in_data, max_length=128, batch_size=2)
        elif args.ranking_model == "dragon_plus":
            print("Calculating DRAGON+ Embeddings of Questions in Prompts ... ")
            questions_in_prompts_embeddings = get_dragon_plus_embeddings_for_query(questions_in_examplars, max_length=128, batch_size=2)
            print("Calculating DRAGON+ Embeddings of Questions in Data ... ")
            questions_in_data_embeddings = get_dragon_plus_embeddings_for_query(questions_in_data, max_length=128, batch_size=2)
        elif args.ranking_model == "e5":
            print("Calculating E5 Embeddings of Questions in Prompts ... ")
            questions_in_prompts_embeddings = get_e5_embeddings_for_query(questions_in_examplars, max_length=128, batch_size=2)
            print("Calculating E5 Embeddings of Questions in Data ... ")
            questions_in_data_embeddings = get_e5_embeddings_for_query(questions_in_data, max_length=128, batch_size=2)
        similarities = torch.matmul(questions_in_data_embeddings, questions_in_prompts_embeddings.T)
        ranked_prompt_indices = torch.argsort(similarities, dim=1, descending=True)
        for example, one_ranked_prompt_indices in zip(data, ranked_prompt_indices):
            example["ranked_prompt_indices"] = one_ranked_prompt_indices.tolist()

    global tokenizer, token_id_to_choice_map
    for example in tqdm(data, desc="Generating reasoning chains", total=len(data)):

        question = example["question"]
        triples, triple_positions = [], []
        for ctx in example["ctxs"]:
            for triple_item in ctx["triples"]:
                triples.append("<{}; {}; {}>".format(triple_item["head"], triple_item["relation"], triple_item["tail"]))
                triple_positions.append(triple_item["position"])
        
        num_total_triples = len(triples)
        if args.ranking_model == "e5_mistral":
            triples_embeddings = get_e5_mistral_embeddings_for_document(triples, max_length=128, batch_size=2)
        elif args.ranking_model == "dragon_plus":
            triples_embeddings = get_dragon_plus_embeddings_for_document(triples, max_length=128, batch_size=2)
        elif args.ranking_model == "e5":
            triples_embeddings = get_e5_embeddings_for_document(triples, max_length=128, batch_size=2)

        paths = [[]]
        paths_scores = [1.0]
        paths_finished = [False]
        for j in range(args.max_chain_length):
            if np.sum(paths_finished) == args.num_chains:
                break
            queries = [
                "knowledge triples: {}\nquestion: {}".format(
                    " ".join([triples[idx] for idx in path]), question
                )
                for path in paths
            ]
            if args.ranking_model == "e5_mistral":
                queries_embeddings = get_e5_mistral_embeddings_for_query("retrieve_relevant_triples", queries, max_length=256, batch_size=1)
            elif args.ranking_model == "dragon_plus":
                queries_embeddings = get_dragon_plus_embeddings_for_query(queries, max_length=256, batch_size=2)
            elif args.ranking_model == "e5":
                queries_embeddings = get_e5_embeddings_for_query(queries, max_length=256, batch_size=2)
            queries_triples_similarities = torch.matmul(queries_embeddings, triples_embeddings.T) # n_path, n_triples 

            candidate_triples_mask = torch.ones_like(queries_triples_similarities)
            for k, path in enumerate(paths):
                candidate_triples_mask[k, path] = 0.0 
            queries_triples_similarities = queries_triples_similarities + \
                torch.finfo(queries_triples_similarities.dtype).min * (1.0 - candidate_triples_mask)
            topk_most_relevant_triples_indices = torch.topk(queries_triples_similarities, k=min(args.num_choices, num_total_triples), dim=1)[1].tolist()

            prompts = get_llama3_generate_reasoning_chains_prompts_chat_format(
                args = args, 
                hop = j, 
                question = question,
                existing_triples = [[triples[idx] for idx in path] for path in paths],
                candidate_triples = [
                    [triples[idx] for idx in candidate_triples_indices] \
                        for candidate_triples_indices in topk_most_relevant_triples_indices
                ],
                ranked_prompt_indices = example.get("ranked_prompt_indices", None)
            )
            inputs = tokenizer_encode_chat_format_for_instruction_model(prompts, args.max_length)
            generated_token_ids, generated_token_logits = model_generate(inputs, max_new_tokens=args.max_new_tokens, batch_size=2)

            answer_token_indices = get_answer_token_indices(args.num_choices, generated_token_ids)
            answer_token_logits = generated_token_logits.gather(1, \
                answer_token_indices[:, None, None].expand(-1, -1, generated_token_logits.shape[-1]))
            answer_token_logits = answer_token_logits.squeeze(1)

            choices_token_ids_list = list(token_id_to_choice_map.keys())
            choices_list = [token_id_to_choice_map[token_id] for token_id in choices_token_ids_list]
            answer_token_probs = F.softmax(answer_token_logits[:, choices_token_ids_list], dim=1)

            new_paths, new_paths_scores, new_paths_finished = [], [], []
            topk_choices_probs, topk_choices_indices = torch.topk(answer_token_probs, k=args.num_beams, dim=1)

            for i in range(len(paths)):
                if paths_finished[i]:
                    new_paths.append(paths[i])
                    new_paths_scores.append(paths_scores[i])
                    new_paths_finished.append(True)
                    continue 
                if torch.all(torch.isnan(topk_choices_probs[i])):
                    print("No choice in generated results! generated text: {}".format(tokenizer.decode(generated_token_ids[i])))
                    new_paths.append(paths[i])
                    new_paths_scores.append(paths_scores[i])
                    new_paths_finished.append(False)
                    continue 
                for b in range(args.num_beams):
                    if torch.isnan(topk_choices_probs[i, b]) or topk_choices_probs[i, b].item() < args.min_triple_prob:
                        continue
                    current_choice = choices_list[topk_choices_indices[i, b].item()]
                    if current_choice != 'A' and (ord(current_choice)-ord('B') >= len(topk_most_relevant_triples_indices[i])):
                        continue
                    new_paths_scores.append(paths_scores[i]*topk_choices_probs[i, b].item())
                    if current_choice == 'A':
                        new_paths.append(paths[i]+[-1]) 
                        new_paths_finished.append(True)
                    else:
                        new_paths.append(paths[i]+[topk_most_relevant_triples_indices[i][ord(current_choice)-ord('B')]])
                        new_paths_finished.append(False)
            
            assert len(new_paths) == len(new_paths_scores)
            assert len(new_paths) == len(new_paths_finished)
            new_paths_sorted_indices = sorted(range(len(new_paths_scores)), key=lambda x: new_paths_scores[x], reverse=True)
            topk_new_paths_sorted_indices = new_paths_sorted_indices[:args.num_chains]
            paths = [new_paths[idx] for idx in topk_new_paths_sorted_indices]
            paths_scores = [new_paths_scores[idx] for idx in topk_new_paths_sorted_indices]
            paths_finished = [new_paths_finished[idx] for idx in topk_new_paths_sorted_indices]
        
        example["chains"] = [
            {
                "triples":[
                    {
                        "triple": triples[triple_index], 
                        "triple_position": triple_positions[triple_index]
                    } 
                    for triple_index in path if triple_index >= 0 
                ],
                "score": path_score
            }
            for path, path_score in zip(paths, paths_scores)
        ]
    
    print(f"saving data to {save_data_file} ... ")
    os.makedirs(os.path.dirname(save_data_file), exist_ok=True)
    save_json(data, save_data_file, use_indent=True)


if __name__ == "__main__":

    args = setup_parser()
    construct_reasoning_chains(args)