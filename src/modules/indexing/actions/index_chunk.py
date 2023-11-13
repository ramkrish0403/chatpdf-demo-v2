from src.clients.chromadb.index import chroma_collection
from src.util.string_util import random_string
import json


def index_chunk(chunk):
    chroma_collection.add(
        documents=[chunk["text"]],
        metadatas=[{"ids": json.dumps(chunk["ids"])}],
        ids=[random_string()]
    )
    return