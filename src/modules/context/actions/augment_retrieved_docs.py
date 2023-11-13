
def update_score(docs, ids, score):
    for id1 in ids:
        docs[id1] = docs.get(id1, 0) + score
    return docs

def augment_retrieved_docs(docs, neighbor_score_factor=0.5, neighborhood_range=5, min_score=0.7):
    augmented_docs = dict()
    for doc in docs:
        ids = doc['ids']
        # print("original ids: ", ids)
        score = doc['score']
        len_ids = len(ids)
        augmented_docs = update_score(augmented_docs, ids, score)
        for i in range(neighborhood_range):
            step = i + 1
            neighbor_score = score * (neighbor_score_factor ** step)

            neighbors = [x+step*len_ids for x in ids]
            # print("neighbors: ", neighbors)
            augmented_docs = update_score(augmented_docs, neighbors, neighbor_score)

            neighbors = [x-step*len_ids for x in ids]
            # print("neighbors: ", neighbors)
            augmented_docs = update_score(augmented_docs, neighbors, neighbor_score)

    # Filter out docs with score less than min_score
    augmented_docs = {k: v for k, v in augmented_docs.items() if v >= min_score}
    return augmented_docs


if __name__ == '__main__':
    docs = [{'score': 0.6475489735603333, 'document': 'Note that the specific terms of your employment relationship, including termination procedures, are governed by the laws of the state in which you are employed. In appropriate circumstances, management will first provide you with a verbal warning, then with one or more written warnings, and if the conduct is not sufficiently altered, eventual demotion, transfer, forced leave, or termination of employment.', 'ids': [192, 193]}, {'score': 0.6394016742706299, 'document': 'Those who retaliate against others for reporting a possible deviation from this policy or for cooperating in an investigation will be subject to disciplinary action, up to and including termination. Nothing in this policy is designed to interfere with, restrain, or prevent employees from communications regarding wages, hours, or other terms and conditions of employment, or to restrain employees in exercising any other right protected by law.', 'ids': [382, 383]}, {'score': 0.6225121021270752, 'document': 'Note that the specific terms of your employment relationship, including termination procedures, are governed by the laws of the state in which you are employed. In appropriate circumstances, management will first provide you with a verbal warning, then with one or more written warnings, and if the conduct is not sufficiently altered, eventual demotion, transfer, forced leave, or termination of employment. Your Manager will make every effort possible to allow you to respond to any disciplinary action taken. Understand that while the Company is concerned with consistent enforcement of our policies, we are not obligated to follow any disciplinary or grievance procedure and, depending on the circumstances, you may be disciplined or terminated without any prior warning or procedure.', 'ids': [192, 193, 194, 195]}, {'score': 0.6177151203155518, 'document': 'Violations If you violate this policy, you will be subject to corrective action, up to and including termination of employment. If necessary, the Company will also advise law enforcement officials of any illegal conduct.', 'ids': [407, 408]}]

    resp = augment_retrieved_docs(docs)
    print(resp)

    # Usage:
    # python src/modules/context/actions/augment_retrieved_docs.py
