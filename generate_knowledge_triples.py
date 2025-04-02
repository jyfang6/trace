import os
import re 
import time 
import pickle
import argparse
import numpy as np
from copy import deepcopy 
from tqdm import trange, tqdm
from typing import Union, Optional, Tuple, List, Dict

import torch 
from torch import Tensor
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel 
from transformers import logging as hf_logging
hf_logging.set_verbosity_error()

from utils.utils import * 
from utils.const import HF_TOKEN 
from prompts import generate_knowledge_triples_template, generate_knowledge_triples_chat_template

tokenizer = None 
model = None 
tokenizer_name_or_path = "meta-llama/Meta-Llama-3-8B-Instruct"
model_name_or_path = "meta-llama/Meta-Llama-3-8B-Instruct"
device = torch.device("cuda")


def setup_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset", type=str, default="hotpotqa")
    parser.add_argument("--batch_size", type=int, default=10)
    parser.add_argument("--max_length", type=int, default=2048)
    parser.add_argument("--max_new_tokens", type=int, default=512)
    parser.add_argument("--num_examplars", type=int, default=3)
    parser.add_argument("--input_data_file", type=str, default="data/hotpotqa/dev.json")
    parser.add_argument("--save_data_file", type=str, default="data/hotpotqa/dev_with_kgs.json")
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
    model_torch_dtype = torch.bfloat16 
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path, torch_dtype=model_torch_dtype, token=HF_TOKEN)
    model.to(device)
    model.eval()
    return model 


def get_dataset_demonstrations(dataset):

    if dataset == "hotpotqa":
        from prompts import generate_knowledge_triples_hotpotqa_examplars
        demonstrations = generate_knowledge_triples_hotpotqa_examplars
    elif dataset == "2wikimultihopqa":
        from prompts import generate_knowledge_triples_2wikimultihopqa_examplars
        demonstrations = generate_knowledge_triples_2wikimultihopqa_examplars
    elif dataset == "musique":
        from prompts import generate_knowledge_triples_musique_examplars
        demonstrations = generate_knowledge_triples_musique_examplars
    else:
        raise ValueError(f"{dataset} is not a supported dataset!")
    
    return demonstrations
    

def get_document_prompts_chat_format_for_instruction_model(args, document_list: List[Dict[str, Optional[Union[str, List[str], List[int]]]]]):

    # document_list: [{"title": str, "sentences": [str], "ranked_prompt_indices": [int] / None}]

    global tokenizer 
    tokenizer = get_tokenizer() if tokenizer is None else tokenizer 

    def convert_several_examplars_to_text(examplars):
        return "\n\n".join(examplars)

    def vary_num_examplars_based_on_context_window(examplars, title, text):

        final_examplars = None

        while len(examplars) > 0:
            for num in range(len(examplars), 0, -1):
                possible_prompt = generate_knowledge_triples_template.format(
                    examplars=convert_several_examplars_to_text(examplars[:num]),
                    title=title, 
                    text=text, 
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
    for i, document in enumerate(document_list):

        title = document["title"]
        sentences = document["sentences"]
        text = " ".join(sentences)

        dataset_demonstrations = get_dataset_demonstrations(args.dataset)
        ranked_prompt_indices = document.get("ranked_prompt_indices", None)
        if ranked_prompt_indices is None:
            ranked_prompt_indices = np.random.permutation(len(dataset_demonstrations))

        examplars = [dataset_demonstrations[idx] for idx in ranked_prompt_indices[:args.num_examplars]]
        examplars = ["Title: {}\nText: {}\nKnowledge Triples: {}".format(example["title"], example["text"], example["triples"]) for example in examplars]
        examplars = vary_num_examplars_based_on_context_window(examplars, title, text)
        # LLaMA3 Format 
        prompts.append(
            [
                {"role": "system", "content": generate_knowledge_triples_chat_template.format(examplars=convert_several_examplars_to_text(examplars))},
                {"role": "user", "content": f"Title: {title}\nText: {text}\nKnowledge Triples: "},
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


def model_generate(inputs: Dict[str, Tensor], max_new_tokens: int=100) -> Tensor:
    global model 
    model = get_model() if model is None else model 
    inputs = to_device(inputs, device)
    generated_token_ids = model.generate(**inputs, max_new_tokens=max_new_tokens, use_cache=True, temperature=1.0, do_sample=False) 
    return generated_token_ids 


def parse_model_output(triples_text: str) -> Tuple:

    results = [] 
    for one_triple_text in re.findall(r'<([^>]*)>', triples_text):
        pieces = one_triple_text.rsplit(";", maxsplit=2)
        if len(pieces) != 3:
            print(f"Something wrong with this triple: \"{one_triple_text}\", Skip this triple!")
            continue
        head, relation, tail = pieces
        results.append((head.strip(), relation.strip(), tail.strip()))
    
    return results


def generate_triples_for_document_list(args, document_list: List[Dict[str, Optional[Union[str, List[str], List[int]]]]], verbose=False) -> List[List[Dict[str, Union[str, list]]]]:

    global tokenizer 

    if verbose:
        progress_bar = trange((len(document_list)-1) // args.batch_size + 1, desc="Generating Knowledge Triples")

    generated_contents = [] 
    for i in range((len(document_list)-1) // args.batch_size + 1): 
        batch_document_list = document_list[i*args.batch_size: (i+1)*args.batch_size]
        batch_prompts = get_document_prompts_chat_format_for_instruction_model(args, batch_document_list)
        batch_inputs = tokenizer_encode_chat_format_for_instruction_model(batch_prompts, args.max_length)
        batch_generated_token_ids = model_generate(batch_inputs, args.max_new_tokens)
        batch_generated_token_ids = batch_generated_token_ids[:, batch_inputs["input_ids"].shape[1]:]
        batch_generated_texts = tokenizer.batch_decode(batch_generated_token_ids, skip_special_tokens=True)
        generated_contents.extend(batch_generated_texts)
        if verbose:
            progress_bar.update(1)
    
    # parse model_outputs 
    results = [] 
    for j, (document, generated_content) in enumerate(zip(document_list, generated_contents)):
        triples = parse_model_output(generated_content) # [(head, relation, tail)]
        document_text = " ".join(document["sentences"])
        triples_in_one_document = []
        for head, relation, tail in triples:
            if head.lower() != document["title"].lower():
                if head.lower() not in document_text.lower():
                    head = document["title"]
            
            triples_in_one_document.append(
                {
                    "head": head,
                    "relation": relation, 
                    "tail": tail, 
                }
            )
        results.append(triples_in_one_document)

    return results


def add_sentence_index_to_generated_triples(
    document_list: List[Dict[str, Optional[Union[str, List[str], List[int]]]]], 
    triples_list: List[List[Dict[str, str]]]
)->List[List[dict]]:
    
    # document_list: [{"title": str, "sentences": [str], "ranked_prompt_indices": [int] / None}]
    # triples_list: [ [{"head": str, "relation": str, "tail": str}] ]
    def get_common_word_count(substring, text):
        return np.sum([word in text for word in substring.split()])
    
    for document, triples in zip(document_list, triples_list):
        sentences = document["sentences"]
        start_sentence_index = 0
        for triple in triples:
            triple_text = triple["relation"] + " " + triple["tail"]
            triple_sentence_common_word_count = \
                [-100] * start_sentence_index + [get_common_word_count(triple_text, sentence) for sentence in sentences[start_sentence_index:]]
            index = int(np.argmax(triple_sentence_common_word_count))
            if index == start_sentence_index + 1:
                start_sentence_index = index
            triple["position"] = [None, index]
    
    return triples_list


def generate_document_knowledge_graph(args):
    """
    (1) KG GENERATION STEP: Main function that orchestrates the knowledge graph generation process
    
    This function extracts knowledge triples from documents in the form of <head entity; relation; tail entity>.
    The process includes:
    1. Loading documents from input data
    2. Identifying unique documents to avoid redundant processing
    3. Generating knowledge triples using an LLM with in-context examples
    4. Adding sentence indices to locate triples in original documents
    5. Storing triples and their positions in the document collection
    
    Args:
        args: Contains parameters like input/output file paths, model parameters, etc.
    """

    data_file, save_data_file = args.input_data_file, args.save_data_file 

    if os.path.exists(save_data_file):
        print(f"{save_data_file} already exists, skip this ...")
        return
    
    # create directory
    os.makedirs(os.path.dirname(save_data_file), exist_ok=True)
    
    print(f"loading data from {data_file} ...")
    data = load_json(data_file)

    # obtain unique documents from the input data 
    id2document = {}
    for example in tqdm(data, desc="Obtaining Unique documents", total=len(data)):
        for ctx in example["ctxs"]:
            document_hash_id = hash_object(ctx["title"] + " " + ctx["text"])
            if document_hash_id in id2document:
                assert ctx["title"] == id2document[document_hash_id]["title"] # the title must be the same 
                continue
            id2document[document_hash_id] = {
                "title": ctx["title"], 
                "sentences": ctx["sentences"],
                "ranked_prompt_indices": ctx.get("ranked_prompt_indices", None), 
            }
    print(f"Successfully get {len(id2document)} unique documents!")

    # obtain KG triples for unique documents 
    document_id_list = list(id2document.keys())
    document_id_to_index = {document_id: i for i, document_id in enumerate(document_id_list)}
    document_list = [id2document[document_id] for document_id in document_id_list]

    tmp_document_triples_file = os.path.join(
        os.path.dirname(save_data_file), 
        "tmp_"+os.path.basename(save_data_file).split(".")[0]+".pkl"
    )
    if os.path.exists(tmp_document_triples_file):
        print(f"{tmp_document_triples_file} already exists, loading cached file...")
        document_triples_list = pickle.load(open(tmp_document_triples_file, "rb"))
    else:
        document_triples_list = generate_triples_for_document_list(args, document_list, verbose=True)
        pickle.dump(document_triples_list, open(tmp_document_triples_file, "wb"))

    torch.cuda.empty_cache()
    # obtain sentence index
    document_triples_with_sentence_index_list = [] 
    batch_size = 50000
    for i in trange((len(document_list) - 1) // batch_size + 1, desc="Finding triple sentence index"):
        batch_document_list = document_list[i*batch_size: (i+1)*batch_size]
        batch_document_triples_list = document_triples_list[i*batch_size: (i+1)*batch_size]
        document_triples_with_sentence_index_list.extend(
            add_sentence_index_to_generated_triples(batch_document_list, batch_document_triples_list)
        )

    # obtain document index 
    for example in tqdm(data, desc="Obtaining document triples", total=len(data)):
        for i, ctx in enumerate(example["ctxs"]):
            document_hash_id = hash_object(ctx["title"] + " " + ctx["text"])
            document_triples = document_triples_with_sentence_index_list[document_id_to_index[document_hash_id]] # [{"head": str, "relation": str, "tail": str, "position": [None, sentence_index]}]
            document_triples = deepcopy(document_triples)
            for triple in document_triples:
                triple["position"][0] = i 
            ctx["triples"] = document_triples
    
    save_json(data, save_data_file, use_indent=True)
    print(f"Successfully save data to {save_data_file} ...")

    if os.path.exists(tmp_document_triples_file):
        os.remove(tmp_document_triples_file)



if __name__ == "__main__":

    args = setup_parser()

    # generate knowledge triples for documents 
    generate_document_knowledge_graph(args)