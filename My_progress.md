1. KG Generation
This is implemented in generate_knowledge_triples.py, which:

Takes documents as input and generates knowledge triples in the form of <head entity; relation; tail entity>
Uses LLaMA3 model to extract these triples from document text
Leverages prompt templates and dataset-specific demonstrations to guide the model
The function includes specialized prompt templates for different datasets (HotpotQA, 2WikiMultiHopQA, MuSiQue) to ensure appropriate knowledge extraction.

2. Reasoning Chain Construction
This is the most sophisticated part, implemented in construct_reasoning_chains.py, which:

Takes the generated knowledge graph (triples) as input
Uses an autoregressive approach to build reasoning chains through the following steps:
Computes embeddings for all knowledge triples using retriever models (e5-mistral, dragon-plus, or e5)
Iteratively constructs reasoning paths by selecting relevant triples
For each step (hop), uses a retrieval model to find candidate triples relevant to the current path
Uses prompts to guide LLaMA3 to select the most appropriate next triple for each path
Maintains multiple candidate paths with scores and extends them using beam search
Terminates paths when they're determined to be complete (when "A. no need for additional knowledge triples" is selected)
Stores the highest-scoring paths for each question

3. Answer Generation
This is implemented in evaluation.py, which:

Takes the constructed reasoning chains as input
Provides different context types for answer generation:
"triples" mode (TRACE-Triple): uses the reasoning chains directly as context
"documents" mode (TRACE-Doc): uses the chains to retrieve original documents for context
"all_documents" mode: uses all documents as context
Uses reader models (LLaMA3, Mistral, or Gemma) to generate the final answer based on the provided context
The different reader models are handled through collators (in collators.py), which prepare the prompt format for each model type.

