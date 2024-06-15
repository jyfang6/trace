import random
import logging
from torch.utils.data import Dataset
from utils.utils import load_json

logger = logging.getLogger(__name__)

class ReaderDataset(Dataset):

    def __init__(self, data_path, n_context=None, chain_key="chains", question_prefix='question:', title_prefix='title:', passage_prefix='context:', **kwargs):
        self.n_context = n_context
        self.chain_key = chain_key
        self.question_prefix = question_prefix
        self.title_prefix = title_prefix
        self.passage_prefix = passage_prefix
        self.kwargs = kwargs
        self.is_train_dataset = True if "train" in data_path else False
        self.data = self.load_data(data_path)
        self.sort_data()

    def load_data(self, data_path):
        pass
    
    def sort_data(self):
        pass

    def __len__(self):
        return len(self.data)

    def get_target(self, example):
        if 'target' in example:
            target = example['target']
            return target
        elif 'answers' in example:
            return random.choice(example['answers']) 
        else:
            logger.warning("Couldn't find target or answers!")
            return None
    
    def get_example(self, index):
        return self.data[index]
    
    def __getitem__(self, index):
        return self.get_example(index)


class ReaderDatasetWithChains(ReaderDataset):

    def load_data(self, data_path):
        logger.info("Loading data from {} ... ".format(data_path))
        data = load_json(data_path)
        examples = [] 
        for k, example in enumerate(data):
            if not "id" in example:
                example["id"] = k 
            for j, chain in enumerate(example.get(self.chain_key, [])):
                if "score" not in chain:
                    chain["score"] = 1.0 / (j+1)
            examples.append(example)
        
        max_scores_list = []
        for example in data:
            scores = [] 
            for chain in example.get(self.chain_key, []):
                scores.append(chain["score"])
            if len(scores) > 0:
                max_scores_list.append(max(scores))
        self.threshold = min(max_scores_list) if len(max_scores_list)>=0 else 0.0 
        return examples 
    
    def sort_data(self):
        if self.n_context is None or not self.chain_key in self.data[0] or not 'score' in self.data[0][self.chain_key][0]:
            return
        for example in self.data:
            example[self.chain_key].sort(key=lambda x: float(x['score']), reverse=True)
    
    def __getitem__(self, index):

        example = self.data[index]
        question = (self.question_prefix + " " + example['question']).strip()
        target = self.get_target(example)
        if self.n_context is not None and self.n_context > 0:
            contexts = [{"title": ctx["title"], "sentences": ctx["sentences"]} for ctx in example["ctxs"]]
            chains = []
            for chain in example[self.chain_key][:self.n_context]:
                if chain["score"] >= self.threshold:
                    chains.append(chain)
        else:
            contexts, chains = None, None
        
        item = {
            "index": index, 
            "question": question, 
            "target": target, 
            "answers": example["answers"], 
            "contexts": contexts,
            "chains": chains
        }
        return item 
