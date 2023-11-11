pip install -r requirements.txt

### context search:
- keyword -> improves precision
- semantic -> vector search -> improves recall

### text chunking:
- summarize chunk -> removes superfluous information
- chunk overlap
- cluster the input data from file -> useful when querying
- generate chunk by replacing this, it, that, etc. with the known entities

### query transformation:
- rephrase query using llm
- generate hypothetical response -> use as query
- query compression

### Retrieval:
- heat 

Basic:
- keyword search
- semantic search
- text chunking
- chunk overlap
- heat map


Advanced:
- cluster the input data from file -> useful when querying
- generate chunk by replacing this, it, that, etc. with the known entities
- rephrase query using llm
- generate hypothetical response -> Hyde -> use as query
- summarize chunk -> removes superfluous information
- prompt compression

Existing prompt compression methods like LLMLingua (Jiang et al., 2023a) and
Selective-Context (Li, 2023) that do not consider the content of the question during compression may
retain too much noisy information in the compressed results, leading to inferior performance. In this
paper, LongLLMLingua is designed to enhance LLM’s perception of key information (relevant to
the question) in the prompt, so that the third challenge of inferior performance in long context scenarios could be addressed




Resources:
https://blog.langchain.dev/semi-structured-multi-modal-rag/
https://pub.towardsai.net/rag-pipeline-pitfalls-the-untold-challenges-of-embedding-table-5296b2d8230a
https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnknownVariableType
https://www.reddit.com/r/LocalLLaMA/comments/15mq1ri/what_are_the_text_chunkingsplitting_and_embedding/
https://esteininger.medium.com/building-a-vector-search-engine-using-hnsw-and-cosine-similarity-753fb5268839
https://weaviate.io/developers/weaviate/concepts/vector-index#hnsw
https://weaviate.io/blog/vector-library-vs-vector-database
https://www.reddit.com/r/MachineLearning/comments/12m9pg0/alternatives_to_pinecone_vector_databases_d/

https://safjan.com/techniques-to-boost-rag-performance-in-production/
https://safjan.com/measure-quality-of-embeddings-intrinsic-vs-extrinsic/
https://safjan.com/the-best-vector-databases-for-storing-embeddings/

https://js.langchain.com/docs/use_cases/question_answering/advanced_conversational_qa
https://docs.trychroma.com/integrations/langchain
https://docs.trychroma.com/usage-guide

https://www.promptingguide.ai/techniques/rag
https://odsc.com/speakers/retrieval-augmented-generation-rag-101-building-an-open-source-chatgpt-for-your-data-with-llama-2-langchain-and-pinecone/
https://odsc.com/speakers/retrieval-augmented-generation-rag-101-building-an-open-source-chatgpt-for-your-data-with-llama-2-langchain-and-pinecone/
https://www.anaconda.com/blog/how-to-build-a-retrieval-augmented-generation-chatbot
https://abvijaykumar.medium.com/prompt-engineering-retrieval-augmented-generation-rag-cd63cdc6b00
https://github.com/topics/chatpdf?l=python

https://www.microsoft.com/en-us/research/project/llmlingua/longllmlingua/

https://github.com/microsoft/LLMLingua
https://towardsdatascience.com/similarity-search-with-ivfpq-9c6348fd4db3