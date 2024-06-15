import torch
from copy import deepcopy
from prompts import * 


class CollatorWithChainsChatFormat:

    def __init__(self, tokenizer, text_maxlength, answer_maxlength=25, context_type="triples", **kwargs):

        self.tokenizer = tokenizer 
        self.tokenizer.padding_side = "left" 
        self.text_maxlength = text_maxlength 
        self.answer_maxlength = answer_maxlength
        assert context_type in ["triples", "documents", "all_documents"] 
        self.context_type = context_type
        self.kwargs = kwargs 

    def get_contexts(self, example):

        chains = example["chains"]
        contexts = example["contexts"]

        if self.context_type == "triples":
            chains_list = [] 
            for i, chain in enumerate(chains):
                for triple_item in chain["triples"]:
                    triple = triple_item['triple']
                    triple_sentence = triple.replace("<", "").replace(">", "").replace(";", "", 2)
                    if triple_sentence not in chains_list:
                        chains_list.append(triple_sentence)
        
        if self.context_type == "documents":
            chains_documents_indices_count_dict = {}
            for i, chain in enumerate(chains):
                for triple_item in chain["triples"]:
                    doc_idx, sent_idx = triple_item["triple_position"]
                    if doc_idx >=0:
                        chains_documents_indices_count_dict[doc_idx] = chains_documents_indices_count_dict.get(doc_idx, 0) + 1 
            
            chains_with_documents_list = []
            ranked_chains_documents_indices = sorted(chains_documents_indices_count_dict.items(), key=lambda x: x[1], reverse=True)
            for idx, count in ranked_chains_documents_indices:
                chains_with_documents_list.append("title: {}, text: {}".format(contexts[idx]["title"], " ".join(contexts[idx]["sentences"])))
        
        if self.context_type == "all_documents":
            all_documents_list = ["title: {}, text: {}".format(context_item["title"], " ".join(context_item["sentences"])) for context_item in contexts]
        
        if self.context_type == "triples":
            context_text_list = chains_list 
        elif self.context_type == "documents":
            context_text_list = chains_with_documents_list
        elif self.context_type == "all_documents":
            context_text_list = all_documents_list

        context_text = "\n".join(["{}. {}".format(i+1, text) for i, text in enumerate(context_text_list)])

        return context_text

    def get_prompts_chat_format(self, batch):

        def convert_several_examplars_to_text(examplars):
            return "\n\n".join(examplars)

        prompts = [] 
        has_contexts = batch[0]["chains"] is not None 

        for example in batch:

            if has_contexts:
                instruction = "Given some contexts and a question, please only output the answer to the question."
            else:
                instruction = "Given a question, please only output the answer to the question."
            
            user_input_text = example["question"] 
            if has_contexts:
                user_input_text = "context:\n" + self.get_contexts(example) + "\n" + user_input_text + "\n" + "the correct answer is:"
            else:
                user_input_text = user_input_text + "\n" + "the correct answer is:"
            
            prompts.append(
                [
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": user_input_text}
                ]
            )
        
        return prompts 
    
    def tokenizer_encode(self, prompts):
        texts = self.tokenizer.apply_chat_template(prompts, tokenize=False, add_generation_prompt=True)
        batch_dict = self.tokenizer(texts, max_length=self.text_maxlength, padding=True, truncation=True, return_tensors='pt')
        tokenizer_outputs = {"input_ids": batch_dict["input_ids"], "attention_mask": batch_dict["attention_mask"]}
        return tokenizer_outputs 

    def __call__(self, batch): 
        batch_size = len(batch)
        index = torch.tensor([example['index'] for example in batch])
        prompts = self.get_prompts_chat_format(batch)
        inputs = self.tokenizer_encode(prompts)
        return index, inputs 


class CollatorWithChains(CollatorWithChainsChatFormat):

    def __init__(self, tokenizer, text_maxlength, answer_maxlength=25, context_type="triples", **kwargs):

        self.tokenizer = tokenizer 
        self.tokenizer.padding_side = "left" 
        self.text_maxlength = text_maxlength 
        self.answer_maxlength = answer_maxlength
        assert context_type in ["triples", "documents", "all_documents"] 
        self.context_type = context_type
        self.kwargs = kwargs 

    def get_prompts(self, batch):

        has_contexts = batch[0]["chains"] is not None
        if has_contexts:
            instruction = "Given some contexts and a question, please only output the answer to the question.\n"
        else:
            instruction =  "Given a question, please only output the answer to the question.\n"
        
        prompts_list = [] 
        for example in batch:
            question = example["question"]
            if has_contexts:
                context = "context:\n{}".format(self.get_contexts(example))
                prompt = context + "\n" + question
                prompts_list.append(prompt)
            else:
                prompts_list.append(question)
        
        prompts_list = ["{}{}\nthe correct answer is:".format(instruction, prompt) for prompt in prompts_list]
        return prompts_list

    def tokenizer_encode(self, prompts):
        batch_dict = self.tokenizer(prompts, max_length=self.text_maxlength, padding=True, truncation=True, return_tensors='pt')
        tokenizer_outputs = {"input_ids": batch_dict["input_ids"], "attention_mask": batch_dict["attention_mask"]}
        return tokenizer_outputs 
    
    def __call__(self, batch):
        batch_size = len(batch)
        index = torch.tensor([example['index'] for example in batch])
        prompts = self.get_prompts(batch)
        inputs = self.tokenizer_encode(prompts)
        return index, inputs 