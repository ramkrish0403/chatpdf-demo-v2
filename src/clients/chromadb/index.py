import chromadb

chroma_client = chromadb.Client()
chroma_collection = chroma_client.create_collection(
    name="my_collection", metadata={"hnsw:space": "cosine"})
