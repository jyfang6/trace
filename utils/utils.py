import os 
import re 
import yaml
import json 
import random
import logging 
import numpy as np 
from typing import Union, List

import torch 
import torch.distributed as dist


FLOAT_KEY = set(["learning_rate", "weight_decay"])

class HParams:

    def __init__(self, properties: dict):
        if properties is None:
            properties = {}
        for k, v in properties.items():
            if k in FLOAT_KEY:
                setattr(self, k, float(v))
            else:
                setattr(self, k, v)
    
    def __getattr__(self, name):
        return None or print(f"The {name} can't be found within the class HParams, return None.")
    
    def get_hparams(self):
        return self.__dict__

def parse_yaml(file):

    if file is None:
        return None
    if not os.path.exists(file):
        raise ValueError(f"File {file} does not exist!")
    with open(file, "r") as fin:
        dict_data = yaml.safe_load(fin)
    for k, v in dict_data.items():
        if v == "None" or v == "none":
            dict_data[k] = None
    hparams = HParams(dict_data)
    return hparams

def reader_specific_params(args):
    reader_params = args.reader.get_hparams()
    trainer_params = args.trainer.get_hparams()
    experiment_params = args.experiment.get_hparams()
    new_params = {}
    for k, v in reader_params:
        if k not in trainer_params and k not in experiment_params:
            new_params[k] = v 
    return new_params

def seed_everything(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True

def setup_logger(local_rank, log_file):

    fh = logging.FileHandler(log_file)
    # fh = MFileHandler(log_file)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s: - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.info(f"Rank: {local_rank}, Saving log file to {log_file} ...")

def load_json(path, type="json"):
    assert type in ["json", "jsonl"] # only support json or jsonl format
    if type == "json":
        outputs = json.loads(open(path, "r", encoding="utf-8").read())
    elif type == "jsonl":
        outputs = []
        with open(path, "r", encoding="utf-8") as fin:
            for line in fin:
                outputs.append(json.loads(line))
    else:
        outputs = []
        
    return outputs

def save_json(data, path, type="json", use_indent=False):

    assert type in ["json", "jsonl"] # only support json or jsonl format
    if type == "json":
        with open(path, "w", encoding="utf-8") as fout:
            if use_indent:
                fout.write(json.dumps(data, indent=4))
            else:
                fout.write(json.dumps(data))

    elif type == "jsonl":
        with open(path, "w", encoding="utf-8") as fout:
            for item in data:
                fout.write("{}\n".format(json.dumps(item)))

    return path

def to_device(inputs, device):

    def dict_to_device(data):
        return {k: item.to(device) if torch.is_tensor(item) else item for k, item in data.items()}
    
    if isinstance(inputs, (tuple, list)):
        new_data = [] 
        for item in inputs:
            if isinstance(item, dict):
                new_data.append(dict_to_device(item))
            elif torch.is_tensor(item):
                new_data.append(item.to(device))
            else:
                new_data.append(item)
    elif isinstance(inputs, dict):
        new_data =dict_to_device(inputs)
    else:
        raise TypeError(f"Currently do not support using <{type(inputs)}> as the type of a batch")

    return new_data

def get_file_prefix(file_name):
    if not os.path.isfile(file_name):
        raise ValueError(f"\{file_name}\" is not a file!")
    file = file_name.split("/")[-1]
    file_prefix = file.split(".")[0] if "." in file else file
    return file_prefix

def string_fuzzy_match(text1, text2):
    # Levenshtein会受到句子长度的影响，在这里不是很合适
    # import Levenshtein
    # return Levenshtein.distance(text1, text2)
    import jellyfish
    return jellyfish.jaro_winkler_similarity(text1, text2)

def hash_object(o) -> str:
    """Returns a character hash code of arbitrary Python objects."""
    import hashlib
    import io
    import dill
    import base58

    m = hashlib.blake2b()
    with io.BytesIO() as buffer:
        dill.dump(o, buffer)
        m.update(buffer.getbuffer())
        return base58.b58encode(m.digest()).decode()

def remove_parentheses_content(s):
    # This regex pattern finds all text enclosed in parentheses
    pattern = r'\(.*?\)'
    # Replace the content in parentheses with an empty string
    cleaned_string = re.sub(pattern, '', s).strip()
    return cleaned_string

def convert_triples_to_sentences(triples: Union[str, List[str]]) -> Union[str, List[str]]:

    return_str = False
    if isinstance(triples, str):
        triples = [triples]
        return_str = True

    triples = [triple.replace("<", "").replace(">", "").replace(";", "", 2) for triple in triples]
    if return_str:
        return triples[0]
    else:
        return triples