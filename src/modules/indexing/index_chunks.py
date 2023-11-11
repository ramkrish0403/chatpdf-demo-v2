from src.clients.chromadb.index import chroma_collection
from src.util.string_util import random_string
import json


def index_chunks(chunks):
    chroma_collection.add(
        documents=[chunk["text"] for chunk in chunks],
        metadatas=[{"ids": json.dumps(chunk["ids"])} for chunk in chunks],
        # ids=[random_string() for _ in range(len(chunks))]
        ids=[json.dumps(chunk["ids"]) for chunk in chunks]
    )
    return
