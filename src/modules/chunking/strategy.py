from .text import text_to_sentences
import json


def remove_duplicates(chunks):
    ids = set()
    new_chunks = []
    for chunk in chunks:
        id1 = json.dumps(chunk["ids"])
        if id1 not in ids:
            ids.add(id1)
            new_chunks.append(chunk)
    return new_chunks


def chunk_text(text, max_steps=5):
    chunks = []
    sentences = text_to_sentences(text)
    for i in range(0, len(sentences)):
        for j in range(0, max_steps + 1):
            step = j
            min_index = max(0, i - step)
            max_index = min(len(sentences) - 1, i + step)
            chunk = {
                "ids": list(range(min_index, max_index + 1)),
                "text": " ".join(sentences[min_index:max_index + 1])
            }
            chunks.append(chunk)

    # Remove duplicates
    chunks = remove_duplicates(chunks)
    return chunks


if __name__ == '__main__':
    def tmp():
        a = [1, 2, 3, 4]
        max_steps = 5
        for i in range(0, len(a)):
            for j in range(0, max_steps + 1):
                print(i, j)
                step = j
                min_index = max(0, i - step)
                max_index = min(len(a) - 1, i + step)
                ids = list(range(min_index, max_index + 1))
                print(ids, "\n")

    tmp()
