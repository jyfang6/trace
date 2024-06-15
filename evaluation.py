import os
import logging
import argparse
import numpy as np
from tqdm import tqdm 

import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import logging as hf_logging
hf_logging.set_verbosity_error()

from readers.datasets import ReaderDatasetWithChains
from readers.collators import CollatorWithChainsChatFormat, CollatorWithChains
from readers.metrics import ems, f1_score

from utils.const import * 
from utils.utils import seed_everything, setup_logger, to_device

logger = logging.getLogger(__file__)

READER_NAME_TO_MODEL_NAME_MAP = {
    "llama3": "meta-llama/Meta-Llama-3-8B-Instruct",
    "mistral": "mistralai/Mistral-7B-v0.1",
    "gemma": "google/gemma-7b",
}

COLLATOR_MAP = {
    "llama3": CollatorWithChainsChatFormat,
    "mistral": CollatorWithChains,
    "gemma": CollatorWithChains,
}

def setup_parser():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # dataset 
    parser.add_argument("--reader", type=str, default="llama3")
    parser.add_argument("--text_maxlength", type=int, default=4096)
    parser.add_argument("--answer_maxlength", type=int, default=25)
    parser.add_argument("--test_file", type=str, default=None)
    parser.add_argument("--n_context", type=int, default=None)
    parser.add_argument("--context_type", type=str, default=None)

    # experiment
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save_dir", type=str, default="checkpoint")
    parser.add_argument("--name", type=str, default="llama3")

    args = parser.parse_args()
    assert args.reader in COLLATOR_MAP.keys() # only support ["llama3", "mistral", "gemma"] reader 
    return args

def load_tokenizer(tokenizer_name_or_path, padding_side="left"):
    print(f"loading tokenizer for \"{tokenizer_name_or_path}\" with padding_side: \"{padding_side}\"")
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, padding_side=padding_side, token=HF_TOKEN)
    if tokenizer.pad_token is None or tokenizer.pad_token_id is None:
        print("Missing padding token, setting padding token to eos_token")
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    return tokenizer

def parse_generated_answer_chat_format(answer):

    if "answer is" in answer:
        idx = answer.find("answer is")
        answer = answer[idx+len("answer is"): ].strip()
        if answer.startswith(":"):
            answer = answer[1:].strip()
    return answer

def parse_generated_answer(answer):

    candidate_answers = answer.split("\n")
    answer = ""
    i = 0 
    while len(answer) < 1 and i<len(candidate_answers):
        answer = candidate_answers[i].strip()
        i += 1 
    answer = parse_generated_answer_chat_format(answer)
    return answer

PARSE_FUNCTION_MAP = {
    "llama3": parse_generated_answer_chat_format, 
    "mistral": parse_generated_answer, 
    "gemma": parse_generated_answer
}

def evaluate(args, tokenizer, dataloader, model):

    em_scores_list, f1_scores_list, precision_scores_list, recall_scores_list, num_tokens_list = [], [], [], [], []

    for batch_index, batch_inputs in tqdm(dataloader, desc="Evaluation", total=len(dataloader)):
        batch_inputs = to_device(batch_inputs, DEVICE)
        batch_outputs = model.generate(**batch_inputs, max_new_tokens=args.answer_maxlength, do_sample=False, temperature=1.0)
        batch_generated_token_ids = batch_outputs[:, batch_inputs["input_ids"].shape[1]:].detach().cpu()
        for i, o in enumerate(batch_generated_token_ids):
            ans = tokenizer.decode(o, skip_special_tokens=True)
            ans = PARSE_FUNCTION_MAP[args.reader](ans)
            gold = dataloader.dataset.get_example(batch_index[i])["answers"]
            em_scores_list.append(ems(ans, gold))
            if not ems(ans, gold):
                print(ans, "\t", gold)
            f1, precision, recall = f1_score(ans, gold[0])
            f1_scores_list.append(f1)
            precision_scores_list.append(precision)
            recall_scores_list.append(recall)
            num_tokens_list.append(batch_inputs["attention_mask"][i].sum().item())

    metrics = {}
    metrics["exact_match"] = np.mean(em_scores_list)
    metrics["f1"] = np.mean(f1_scores_list)
    metrics["precision"] = np.mean(precision_scores_list)
    metrics["recall"] = np.mean(recall_scores_list)
    metrics["avg_num_tokens"] = np.mean(num_tokens_list)

    return metrics


if __name__ == "__main__":

    args = setup_parser()
    seed_everything(args.seed)

    checkpoint_path = os.path.join(args.save_dir, args.name)
    if not os.path.exists(checkpoint_path):
        os.makedirs(checkpoint_path, exist_ok=True)
    setup_logger(-1, os.path.join(checkpoint_path, "prediction.log"))

    # load dataset  
    dataset = ReaderDatasetWithChains(data_path=args.test_file, n_context=args.n_context, chain_key="chains")

    # load collator 
    model_name_or_path = READER_NAME_TO_MODEL_NAME_MAP[args.reader]
    tokenizer = load_tokenizer(model_name_or_path, padding_side="left")
    collator = COLLATOR_MAP[args.reader](
        tokenizer = tokenizer, 
        text_maxlength = args.text_maxlength,
        answer_maxlength=args.answer_maxlength, 
        context_type=args.context_type 
    )
    dataloader = DataLoader(dataset, batch_size=args.batch_size, drop_last=False, shuffle=False, collate_fn=collator)
    
    # load model 
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path, token=HF_TOKEN)
    model.to(DEVICE)
    model.eval()

    # evaluate 
    metrics = evaluate(args, tokenizer, dataloader, model)
    logger.info("====================== Evaluation Results ======================")
    logger.info("n_context: {}".format(args.n_context))
    logger.info("context_type: {}".format(args.context_type))
    logger.info(metrics)
    logger.info("================================================================")