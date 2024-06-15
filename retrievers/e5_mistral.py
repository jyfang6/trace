import torch 
from torch import Tensor
from transformers import AutoTokenizer, AutoModel
from typing import Union, List, Dict

from utils.utils import * 

tokenizer = None 
model = None 

INSTRUCTION_MAP = {
    "retrieve_semantically_similar_text": "Retrieve semantically similar text.", 
    "retrieve_relevant_triples": "Given some knowledge triples and a question, retrieve additional knowledge triples that can help answer the question", 
}

tokenizer_name_or_path = 'intfloat/e5-mistral-7b-instruct'
model_name_or_path = 'intfloat/e5-mistral-7b-instruct'
device = torch.device("cuda")


def get_tokenizer():
    return AutoTokenizer.from_pretrained(tokenizer_name_or_path)


def get_model():
    print("loading e5-mistral model in torch.bfloat16 ...")
    model = AutoModel.from_pretrained(model_name_or_path, torch_dtype=torch.bfloat16)
    model.to(device)
    model.eval()
    return model 


def get_query_with_instruction(task: str, query_list: List[str]) -> List[str]:
    task_description = INSTRUCTION_MAP[task]
    f = "Instruct: {desc}\nQuery: {query}"
    query_with_instruction = [f.format(desc=task_description, query=query) for query in query_list]
    return query_with_instruction


def tokenizer_encode(texts: Union[str, List[str]], max_length: int=4096) -> Dict[str, Tensor]:

    global tokenizer 
    tokenizer = get_tokenizer() if tokenizer is None else tokenizer 
    
    if isinstance(texts, str):
        texts = [texts]

    batch_dict = tokenizer(texts, max_length=max_length-1, return_attention_mask=False, padding=False, truncation=True)
    batch_dict["input_ids"] = [input_ids + [tokenizer.eos_token_id] for input_ids in batch_dict['input_ids']]
    batch_dict = tokenizer.pad(batch_dict, padding=True, return_attention_mask=True, return_tensors='pt')
    tokenizer_outputs = {"input_ids": batch_dict["input_ids"], "attention_mask": batch_dict["attention_mask"]}
    return tokenizer_outputs 


def last_token_pool(last_hidden_states: Tensor, attention_mask: Tensor) -> Tensor:

    left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
    if left_padding:
        return last_hidden_states[:, -1]
    else:
        sequence_lengths = attention_mask.sum(dim=1) - 1
        batch_size = last_hidden_states.shape[0]
        return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]


def get_e5_mistral_embeddings(inputs: Dict[str, Tensor]) -> Tensor:

    global model 
    model = get_model() if model is None else model 

    inputs = to_device(inputs, device)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = last_token_pool(outputs.last_hidden_state, inputs["attention_mask"])

    return embeddings


def get_e5_mistral_embeddings_for_query(task: str, query_list: List[str], max_length: int=128, batch_size: int=4) -> Tensor:

    query_with_instruction_list = get_query_with_instruction(task, query_list)

    query_embeddings_list = [] 
    for i in range((len(query_with_instruction_list)-1) // batch_size + 1):
        batch_query_with_instruction_list = query_with_instruction_list[i*batch_size: (i+1)*batch_size]
        batch_query_inputs = tokenizer_encode(batch_query_with_instruction_list, max_length=max_length)
        batch_query_embeddings = get_e5_mistral_embeddings(batch_query_inputs) 
        query_embeddings_list.append(batch_query_embeddings.detach().cpu())
    query_embeddings = torch.cat(query_embeddings_list, dim=0) # num_query, 4096 

    return query_embeddings


def get_e5_mistral_embeddings_for_document(doc_list: List[str], max_length: int=256, batch_size: int=4) -> Tensor:

    doc_embeddings_list = [] 
    for i in range((len(doc_list)-1) // batch_size + 1):
        batch_doc_list = doc_list[i*batch_size: (i+1)*batch_size]
        batch_doc_inputs = tokenizer_encode(batch_doc_list, max_length=max_length)
        batch_doc_embeddings = get_e5_mistral_embeddings(batch_doc_inputs)
        doc_embeddings_list.append(batch_doc_embeddings.detach().cpu())
    doc_embeddings = torch.cat(doc_embeddings_list, dim=0)

    return doc_embeddings 


if __name__ == "__main__":

    task = "retrieve_semantically_similar_text"
    query_list = ["how much protein should a female eat"]
    embeddings = get_e5_mistral_embeddings_for_query(task, query_list)