import json

def normalize_chromadb_query_output(results):
    docs = []
    queries_len = len(results['ids'])
    for i in range(queries_len):
        for j in range(len(results['ids'][i])):
            if not results or not results['ids'] or not results['ids'][i] or not results['ids'][i][j]:
                continue
            distance = results['distances'][i][j]
            similarity = 1 - distance
            ids = json.loads(results['metadatas'][i][j]['ids'])
            document = results['documents'][i][j]
            doc = {
                "score": similarity,
                "document": document,
                "ids": ids
            }
            docs.append(doc)
    # Sort by score in descending order
    docs.sort(key=lambda x: x['score'], reverse=True)
    return docs


if __name__ == '__main__':
    results = {'ids': [['bqsikwijyb', 'lhtmrgztwo', 'wqlcyxmlmk', 'celsxoluny']], 'distances': [[0.35245102643966675, 0.3605983257293701, 0.3774878978729248, 0.38228487968444824]], 'metadatas': [[{'ids': '[192, 193]'}, {'ids': '[382, 383]'}, {'ids': '[192, 193, 194, 195]'}, {'ids': '[407, 408]'}]], 'embeddings': None, 'documents': [['Note that the specific terms of your employment relationship, including termination procedures, are governed by the laws of the state in which you are employed. In appropriate circumstances, management will first provide you with a verbal warning, then with one or more written warnings, and if the conduct is not sufficiently altered, eventual demotion, transfer, forced leave, or termination of employment.', 'Those who retaliate against others for reporting a possible deviation from this policy or for cooperating in an investigation will be subject to disciplinary action, up to and including termination. Nothing in this policy is designed to interfere with, restrain, or prevent employees from communications regarding wages, hours, or other terms and conditions of employment, or to restrain employees in exercising any other right protected by law.', 'Note that the specific terms of your employment relationship, including termination procedures, are governed by the laws of the state in which you are employed. In appropriate circumstances, management will first provide you with a verbal warning, then with one or more written warnings, and if the conduct is not sufficiently altered, eventual demotion, transfer, forced leave, or termination of employment. Your Manager will make every effort possible to allow you to respond to any disciplinary action taken. Understand that while the Company is concerned with consistent enforcement of our policies, we are not obligated to follow any disciplinary or grievance procedure and, depending on the circumstances, you may be disciplined or terminated without any prior warning or procedure.', 'Violations If you violate this policy, you will be subject to corrective action, up to and including termination of employment. If necessary, the Company will also advise law enforcement officials of any illegal conduct.']], 'uris': None, 'data': None}

    resp = normalize_chromadb_query_output(results)
    print(resp)

    # Usage:
    # python src/modules/context/actions/normalize_chromadb_query_output.py
