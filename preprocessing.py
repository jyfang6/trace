import os
import argparse
from tqdm import tqdm

import torch 
from utils.utils import seed_everything, load_json, save_json 
from retrievers.e5_mistral import get_e5_mistral_embeddings_for_query, get_e5_mistral_embeddings_for_document

def setup_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset", type=str, default="hotpotqa")
    parser.add_argument("--num_dev_data", type=int, default=500)
    parser.add_argument("--raw_data_folder", type=str, default="data/hotpotqa/raw_data")
    parser.add_argument("--save_data_folder", type=str, default="data/hotpotqa")
    args = parser.parse_args()
    return args


def convert_hotpotqa_to_uniform_format(example):

    ctxs = []
    for i, (title, sentences) in enumerate(example["context"]):
        sentences = [s.strip() for s in sentences]
        ctxs.append(
            {
                "id": str(i), 
                "title": title, 
                "text": " ".join(sentences), 
                "sentences": sentences
            }
        )

    supporting_facts = [] 
    for supporting_fact_title, supporting_fact_sentence_idx in example["supporting_facts"]:
        supporting_fact_context_index = None
        for i, ctx in enumerate(ctxs):
            if ctx["title"].strip().lower() == supporting_fact_title.strip().lower():
                supporting_fact_context_index = i 
                break 
        if supporting_fact_context_index is None:
            print("Couldn't find supporting fact context index for {}".format((supporting_fact_title, supporting_fact_sentence_idx)))
        supporting_facts.append((supporting_fact_context_index, supporting_fact_sentence_idx))
    
    result = {
        "id": example["_id"], 
        "question": example["question"], 
        "answers": [example["answer"]], 
        "ctxs": ctxs, 
        "supporting_facts": supporting_facts, 
        "type": example["type"], 
        "level": example["level"]
    }

    return result


def convert_2wikimultihopqa_to_uniform_format(example):

    ctxs = [] 
    for i, (title, sentences) in enumerate(example["context"]):
        sentences = [s.strip() for s in sentences]
        ctxs.append(
            {
                "id": str(i), 
                "title": title, 
                "text": " ".join(sentences), 
                "sentences": sentences
            }
        )
    
    supporting_facts = [] 
    for supporting_fact_title, supporting_fact_sentence_idx in example["supporting_facts"]:
        supporting_fact_context_index = None
        for i, ctx in enumerate(ctxs):
            if ctx["title"].strip().lower() == supporting_fact_title.strip().lower():
                supporting_fact_context_index = i 
                break 
        if supporting_fact_context_index is None:
            print("Couldn't find supporting fact context index for {}".format((supporting_fact_title, supporting_fact_sentence_idx)))
        supporting_facts.append((supporting_fact_context_index, supporting_fact_sentence_idx))
    
    result = {
        "id": example["_id"], 
        "question": example["question"], 
        "answers": [example["answer"]], 
        "ctxs": ctxs, 
        "supporting_facts": supporting_facts, 
        "type": example["type"], 
    }

    return result


def convert_musique_to_uniform_format(example):

    import nltk 
    from nltk.tokenize import sent_tokenize

    ctxs = []
    for i, context_item in enumerate(example["paragraphs"]):
        sentences = sent_tokenize(context_item["paragraph_text"])
        ctxs.append(
            {
                "id": str(i), 
                "title": context_item["title"], 
                "text": context_item["paragraph_text"], 
                "sentences": sentences, 
            }
        )
    
    supporting_facts = [] 
    for question_decomposition_item in example["question_decomposition"]:
        sf_ctx_index = question_decomposition_item["paragraph_support_idx"]
        sf_sentence_index = 0 
        for j, sentence in enumerate(ctxs[sf_ctx_index]["sentences"]):
            if question_decomposition_item["answer"].lower() in sentence.lower():
                sf_sentence_index = j 
                break
        supporting_facts.append((sf_ctx_index, sf_sentence_index))
    
    result = {
        "id": example["id"], 
        "question": example["question"], 
        "answers": [example["answer"]] + example["answer_aliases"],
        "ctxs": ctxs, 
        "supporting_facts": supporting_facts, 
        "answerable": example["answerable"]
    }

    return result


UNIFORM_FORMAT_MAP = {
    "hotpotqa": convert_hotpotqa_to_uniform_format,
    "2wikimultihopqa": convert_2wikimultihopqa_to_uniform_format, 
    "musique": convert_musique_to_uniform_format, 
}

DATASET_TRAIN_DEV_FILES = {
    "hotpotqa": {"train": "hotpot_train_v1.1.json", "dev": "hotpot_dev_distractor_v1.json"}, 
    "2wikimultihopqa": {"train": "train.json", "dev": "dev.json"}, 
    "musique": {"train": "musique_ans_v1.0_train.jsonl", "dev": "musique_ans_v1.0_dev.jsonl"}, 
}


def split_train_dev_test_data(args):

    save_folder = args.save_data_folder
    os.makedirs(save_folder, exist_ok=True)

    raw_train_data_file = os.path.join(args.raw_data_folder, DATASET_TRAIN_DEV_FILES[args.dataset]["train"])
    print(f"loading raw training data from {raw_train_data_file} ...")
    raw_train_data = load_json(raw_train_data_file, type=os.path.basename(raw_train_data_file).split(".")[-1])

    raw_dev_data_file = os.path.join(args.raw_data_folder, DATASET_TRAIN_DEV_FILES[args.dataset]["dev"])
    print(f"loading raw dev data from {raw_dev_data_file} ...")
    raw_dev_data = load_json(raw_dev_data_file, type=os.path.basename(raw_dev_data_file).split(".")[-1])

    # obtain development & test sets 
    import numpy as np 
    seed_everything(0)
    indices = np.random.permutation(len(raw_train_data))
    train_data_orig_format = [raw_train_data[i] for i in indices[:-args.num_dev_data]] 
    dev_data_orig_format = [raw_train_data[i] for i in indices[-args.num_dev_data:]]

    # use original development set as test set 
    test_data_orig_format = raw_dev_data

    convert_func = UNIFORM_FORMAT_MAP[args.dataset]
    save_train_data_file = os.path.join(args.save_data_folder, "train.json")
    if not os.path.exists(save_train_data_file):
        train_data_uniform_format = [] 
        for example in tqdm(train_data_orig_format, desc="Converting training data to uniform format"):
            train_data_uniform_format.append(convert_func(example))
        save_json(train_data_uniform_format, save_train_data_file, use_indent=True)
        print(f"Successfully save train data to {save_train_data_file}!")
    else:
        print(f"{save_train_data_file} already exists, Skip this file!")
    
    save_dev_data_file = os.path.join(args.save_data_folder, "dev.json")
    if not os.path.exists(save_dev_data_file):
        dev_data_uniform_format = [] 
        for example in tqdm(dev_data_orig_format, desc="Converting development data to uniform format"):
            dev_data_uniform_format.append(convert_func(example))
        save_json(dev_data_uniform_format, save_dev_data_file, use_indent=True)
        print(f"Successfully save dev data to {save_dev_data_file}!")
    else:
        print(f"{save_dev_data_file} already exists, Skip this file!")
    
    save_test_data_file = os.path.join(args.save_data_folder, "test.json")
    if not os.path.exists(save_test_data_file):
        test_data_uniform_format = [] 
        for example in tqdm(test_data_orig_format, desc="Converting test data to uniform format"):
            test_data_uniform_format.append(convert_func(example))
        save_json(test_data_uniform_format, save_test_data_file, use_indent=True)
        print(f"Successfully save test data to {save_test_data_file}!")
    else:
        print(f"{save_test_data_file} already exists, Skip this file!")


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


def get_document_demonstration_rank(args):

    max_length = 256 
    batch_size = 4 

    dataset_demonstrations = get_dataset_demonstrations(args.dataset)

    print("calculating demonstration embeddings ...")
    demonstration_texts = ["title: {} text: {}".format(demo["title"], demo["text"]) for demo in dataset_demonstrations]
    demonstration_embeddings = get_e5_mistral_embeddings_for_document(
        doc_list=demonstration_texts,
        max_length=max_length, 
        batch_size=batch_size,
    )
    print(f"successfully obtained embeddings for {len(demonstration_texts)} demonstrations! ...")

    for file_type in ["dev", "test"]: 
        file_path = os.path.join(args.save_data_folder, "{}.json".format(file_type))
        print(f"loading data from {file_path} ...")
        data = load_json(file_path)
        for example in tqdm(data, desc=f"Calculating Demonstration Rank", total=len(data)):
            documents = ["title: {} text: {}".format(ctx["title"], ctx["text"]) for ctx in example["ctxs"]]
            documents_embeddings = get_e5_mistral_embeddings_for_query(
                "retrieve_semantically_similar_text",
                query_list=documents, 
                max_length=max_length, 
                batch_size=batch_size, 
            )
            similarities = torch.matmul(documents_embeddings, demonstration_embeddings.T)
            demonstration_rank = torch.argsort(similarities, dim=1, descending=True)
            for i, ctx in enumerate(example["ctxs"]):
                ctx["ranked_prompt_indices"] = demonstration_rank[i].tolist()
        save_json(data, file_path, use_indent=True)


if __name__ == "__main__":

    args = setup_parser()

    # split the data into train, development and test sets 
    split_train_dev_test_data(args)

    # calculate the similarities between documents and documents in the KG generation prompts
    get_document_demonstration_rank(args)