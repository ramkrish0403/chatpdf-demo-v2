from src.clients.chromadb.index import chroma_collection
import json

def get_context(query: str, length: int = 500):
    queries = [query]
    results = chroma_collection.query(
        query_texts=queries,
        n_results=4
    )
    print(results)
    '''
    {'ids': [['vxsrjigtyh', 'tekdhvgqpl']], 'distances': [[1.0680747032165527, 1.1001427173614502]], 'metadatas': [[{'ids': '[900, 901]'}, {'ids': '[371, 372]'}]], 'embeddings': None, 'documents': [['We look forward to working with you to create a successful\nCompany and a safe, productive, and pleasant workplace. Shruti Gupta, CEO\nZania, Inc.\n45 Acknowledgment of Receipt and Review\nBy signing below, I acknowledge that I have received a copy of the Zania, Inc.', 'financial or sales records/reports, marketing or business strategies/plans, product development, customer lists,\npatents, trademarks, etc.) related to the Company.']], 'uris': None, 'data': None}
    '''
    # Generate heat map
    docs = []
    for i in range(len(queries)):
        for j in range(len(results['ids'][i])):
            if not results or not results['ids'] or not results['ids'][i] or not results['ids'][i][j]:
                continue
            distance = results['distances'][i][j]
            similarity = 1 - distance
            ids = json.loads(results['metadatas'][i][j]['ids'])


