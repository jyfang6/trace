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
from transformers import AutoTokenizer, AutoModel 
from utils.utils import * 

tokenizer = None
query_encoder = None 
doc_encoder = None

tokenizer_name_or_path = 'facebook/dragon-plus-query-encoder'
query_encoder_name_or_path = 'facebook/dragon-plus-query-encoder'
doc_encoder_name_or_path = 'facebook/dragon-plus-context-encoder'
device = torch.device("cuda")


def get_tokenizer():
    return AutoTokenizer.from_pretrained(tokenizer_name_or_path)


def get_query_encoder():
    print(f"loading DRAGON+ query checkpoint from {query_encoder_name_or_path} ... ")
    model = AutoModel.from_pretrained(query_encoder_name_or_path)
    model.to(device)
    model.eval()
    return model 


def get_doc_encoder():
    print(f"loading DRAGON+ document checkpoint from {doc_encoder_name_or_path} ... ")
    model = AutoModel.from_pretrained(doc_encoder_name_or_path)
    model.to(device)
    model.eval()
    return model


def tokenizer_encode(texts: List[str], max_length: int):

    global tokenizer
    tokenizer = get_tokenizer() if tokenizer is None else tokenizer

    batch_dict = tokenizer(texts, max_length=max_length, padding=True, truncation=True, return_tensors='pt')
    tokenizer_outputs = {"input_ids": batch_dict["input_ids"], "attention_mask": batch_dict["attention_mask"]}
    return tokenizer_outputs


def get_dragon_plus_embeddings_for_query(query_list: List[str], max_length: int=128, batch_size: int=4) -> Tensor:

    global query_encoder
    query_encoder = get_query_encoder() if query_encoder is None else query_encoder

    query_embeddings_list = []
    for i in range((len(query_list)-1)//batch_size+1):
        batch_query_list = query_list[i*batch_size: (i+1)*batch_size]
        batch_query_inputs = tokenizer_encode(batch_query_list, max_length=max_length)
        batch_query_inputs = to_device(batch_query_inputs, device)
        with torch.no_grad():
            batch_query_embeddings = query_encoder(**batch_query_inputs).last_hidden_state[:, 0, :]
        query_embeddings_list.append(batch_query_embeddings.detach().cpu())
    query_embeddings = torch.cat(query_embeddings_list, dim=0)

    return query_embeddings


def get_dragon_plus_embeddings_for_document(doc_list: List[str], max_length: int=256, batch_size: int=4) -> Tensor:

    global doc_encoder
    doc_encoder = get_doc_encoder() if doc_encoder is None else doc_encoder

    doc_embeddings_list = [] 
    for i in range((len(doc_list)-1)//batch_size+1):
        batch_doc_list = doc_list[i*batch_size: (i+1)*batch_size]
        batch_doc_inputs = tokenizer_encode(batch_doc_list, max_length=max_length)
        batch_doc_inputs = to_device(batch_doc_inputs, device)
        with torch.no_grad():
            batch_doc_embeddings = doc_encoder(**batch_doc_inputs).last_hidden_state[:, 0, :]
        doc_embeddings_list.append(batch_doc_embeddings.detach().cpu())
    doc_embeddings = torch.cat(doc_embeddings_list, dim=0)

    return doc_embeddings