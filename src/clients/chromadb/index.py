import chromadb
import os

# Get absolute path of current directory
current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "data")
# chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path=data_dir)
chroma_collection = chroma_client.get_or_create_collection(
    name="my_collection", metadata={"hnsw:space": "cosine"})
