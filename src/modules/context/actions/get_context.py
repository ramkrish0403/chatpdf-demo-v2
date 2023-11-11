import json
from src.clients.chromadb.index import chroma_collection
from .normalize_chromadb_query_output import normalize_chromadb_query_output
from .augment_retrieved_docs import augment_retrieved_docs


def get_context(query: str, n_results: int = 4, length: int = 500):
    queries = [query]
    results = chroma_collection.query(
        query_texts=queries,
        n_results=n_results
    )
    # print(results)
    # Normalize results
    docs = normalize_chromadb_query_output(results)

    # Augment results
    augmented_doc_ids = augment_retrieved_docs(docs)

    # Get the augmented docs
    # new_query = {
    #     "$or": [{"ids": {"$eq": json.dumps([int(x)])}} for x in augmented_doc_ids.keys()]
    # }
    # new_query = {
    #     "$or": [{"ids": json.dumps([int(x)])} for x in augmented_doc_ids.keys()]
    # }
    ids = [json.dumps([int(x)]) for x in augmented_doc_ids.keys()]
    # print(ids)
    doc_results = chroma_collection.get(
        ids = ids
    )
    # doc_results = chroma_collection.get()
    # print(doc_results)

    # Get the documents from the results in the same order as augmented_doc_ids sorted in ascending order
    sorted_ids = sorted([int(x) for x in augmented_doc_ids.keys()], reverse=False)
    document_dict = dict()
    for i in range(len(sorted_ids)):
        id1 = json.loads(doc_results['ids'][i])[0]
        document = doc_results['documents'][i]
        document_dict[id1] = document
    documents = [document_dict[x] for x in sorted_ids]
    # return " ".join(documents)
    return documents
