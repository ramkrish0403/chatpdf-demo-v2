from .text import text_to_sentences


def chunk_text(text, max_steps=5):
    chunks = []
    sentences = text_to_sentences(text)
    for step_size in range(1, max_steps + 1):
        for i in range(0, len(sentences), step_size):
            '''
            For each sentence, we want to create a chunk that contains the sentence before and after the current sentence.
            For ith sentence, we want to create a chunk that contains the (i-1)th sentence, the (i)th sentence  and the (i+1)th sentence when step_size is 1.
            For ith sentence, we want to create a chunk that contains the (i-2)th sentence, the (i-1)th sentence, the (i) th sentence, the (i+1)th sentence and the (i+2)th sentence when step_size is 2.
            etc.
            '''
            min_index = max(0, i - step_size)
            max_index = min(len(sentences) - 1, i + step_size)
            chunk = {
                "ids": list(range(min_index, max_index)),
                "text": " ".join(sentences[min_index:max_index])
            }
            chunks.append(chunk)
    return chunks
