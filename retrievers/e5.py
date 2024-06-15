import os
import glob 
import pickle
import logging
import argparse
import numpy as np
from tqdm import tqdm
from typing import Union, Optional, List, Dict

import torch
from torch import Tensor
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel
from utils.utils import * 

tokenizer = None
model = None 
tokenizer_name_or_path = 'intfloat/e5-large-v2'
model_name_or_path = 'intfloat/e5-large-v2'
device = torch.device("cuda")

def get_tokenizer():
    return AutoTokenizer.from_pretrained(tokenizer_name_or_path)


def get_model():
    print(f"loading E5 checkpoint from {model_name_or_path} ... ")
    model = AutoModel.from_pretrained(model_name_or_path)
    model.to(device)
    model.eval()
    return model 


def tokenizer_encode(texts: List[str], max_length: int):

    global tokenizer
    tokenizer = get_tokenizer() if tokenizer is None else tokenizer

    batch_dict = tokenizer(texts, max_length=max_length, padding=True, truncation=True, return_tensors='pt')
    tokenizer_outputs = {"input_ids": batch_dict["input_ids"], "attention_mask": batch_dict["attention_mask"]}
    return tokenizer_outputs


def average_pool(last_hidden_states: Tensor, attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]


def model_encode(inputs: Dict[str, Tensor]) -> Tensor:

    global model, tokenizer
    model = get_model() if model is None else model

    inputs = to_device(inputs, device)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = average_pool(outputs.last_hidden_state, inputs['attention_mask'])
    embeddings = F.normalize(embeddings, p=2, dim=1)
    return embeddings 


def get_e5_embeddings_for_query(query_list: List[str], max_length: int=128, batch_size: int=4) -> Tensor:

    def append_query_symbol(query_list):
        return ["query: " + query for query in query_list]
    
    query_list = append_query_symbol(query_list)
    query_embeddings_list = [] 
    for i in range((len(query_list) - 1) // batch_size + 1):
        batch_query_list = query_list[i*batch_size: (i+1)*batch_size]
        batch_query_inputs = tokenizer_encode(batch_query_list, max_length=max_length)
        batch_query_embeddings = model_encode(batch_query_inputs)
        query_embeddings_list.append(batch_query_embeddings.detach().cpu())
    query_embeddings = torch.cat(query_embeddings_list, dim=0)

    return query_embeddings

def get_e5_embeddings_for_document(doc_list: List[str], max_length: int=256, batch_size: int=4) -> Tensor:

    def append_document_symbol(doc_list): 
        return ["passage: " + doc for doc in doc_list]
    
    doc_list = append_document_symbol(doc_list)
    doc_embeddings_list = [] 
    for i in range((len(doc_list) - 1) // batch_size + 1):
        batch_doc_list = doc_list[i*batch_size: (i+1)*batch_size]
        batch_doc_inputs = tokenizer_encode(batch_doc_list, max_length=max_length)
        batch_doc_embeddings = model_encode(batch_doc_inputs)
        doc_embeddings_list.append(batch_doc_embeddings.detach().cpu())
    doc_embeddings = torch.cat(doc_embeddings_list, dim=0)

    return doc_embeddings
