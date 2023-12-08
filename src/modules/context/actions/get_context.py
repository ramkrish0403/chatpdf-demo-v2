import json
from src.clients.chromadb.index import chroma_collection
from .normalize_chromadb_query_output import normalize_chromadb_query_output
from .augment_retrieved_docs import augment_retrieved_docs
from .get_hypothetical_response import get_hypothetical_response


def get_context(query: str, n_results: int = 4, length: int = 500):
    # Generate hypothetical response
    # hypothetical_response = get_hypothetical_response(query)
    queries = [query]
    # queries = [query, hypothetical_response]
    results = chroma_collection.query(
        query_texts=queries,
        n_results=n_results
    )
    # print(results)
    # print("Chromadb docs top_k: \n", json.dumps(results, indent=4))
    # Normalize results
    docs = normalize_chromadb_query_output(results)
    # print("Chromadb docs normalized: \n", json.dumps(docs, indent=4))

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
    # print(len(doc_results['ids']), len(augmented_doc_ids.keys()))
    # print(doc_results['ids'])
    # doc_results = chroma_collection.get()
    # print(doc_results)
    # print("Chromadb docs: \n", json.dumps(doc_results, indent=4))

    document_dict = dict()
    for (id1, document) in zip(doc_results['ids'], doc_results['documents']):
        id1 = json.loads(id1)[0]
        document_dict[id1] = document

    # Get the documents from the results in the same order as augmented_doc_ids sorted in ascending order
    sorted_ids = sorted([int(x)
                        for x in augmented_doc_ids.keys()], reverse=False)
    documents = [document_dict[x] for x in sorted_ids if x in document_dict.keys()]
    # return " ".join(documents)
    return documents
