import chromadb
from chromadb.utils import embedding_functions
import os

# Get absolute path of current directory
current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "data")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ.get("OPENAI_API_KEY"),
    model_name="text-embedding-ada-002"
)

# chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path=data_dir)
chroma_collection = chroma_client.get_or_create_collection(
    name="my_collection", 
    metadata={"hnsw:space": "cosine"},
    # embedding_function=openai_ef,
)
