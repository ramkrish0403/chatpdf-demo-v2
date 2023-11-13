import os
import sys
from pathlib import Path


# Add the top-level folder of the project to sys.path
top_level_dir = str(Path(__file__).resolve().parent.parent)
if top_level_dir not in sys.path:
    sys.path.append(top_level_dir)


from modules.extractors.index import extractPDF
from modules.chunking.index import chunk_text
from modules.indexing.index import index_chunks
from modules.context.index import get_context
# from modules.prompt_compression.index import get_longLLMLingua_compressed_prompt
from modules.openai.index import get_completion


def listFiles():
    # List files
    data_folder = os.path.join(os.path.dirname(__file__), 'data')
    # print(data_folder)
    files = [os.path.join(data_folder, x)
             for x in os.listdir(data_folder) if x.endswith(".pdf")]
    return files


def main(to_index=False):
    if (to_index):
        files = listFiles()
        # print(files)
        if len(files) == 0:
            print("No pdf files found")
            return

        # Extract text
        file = files[0]
        text = extractPDF(file)
        print(len(text))

        # Sanitize text
        text = text.replace("\n", " ")

        # Chunk text
        chunks = chunk_text(text)
        print(len(chunks))
        # print(chunks[-1])

        # index the chunks
        print("Indexing chunks...")
        index_chunks(chunks)

    # query the chunks
    '''
    What is the name of the company?
    Who is the CEO of the company?
    What is their vacation policy?
    What is the termination policy?
    '''
    print("Querying...")
    query = "What is their vacation policy?"
    context = get_context(query, n_results=10)
    # print(context)
    # context_joined = ' '.join(context)
    context_joined = '\n'.join(context)
    # print('context_joined)

    # Get the compressed prompt
    # compressed_prompt = get_longLLMLingua_compressed_prompt(
    #     context=context,
    #     query=query,
    #     instruction="Answer the question based on the context retrieved from the employee handbook."
    # )
    # print(compressed_prompt)

    # prompt = compressed_prompt
    instruction = "Answer the question based on the context retrieved from the employee handbook.Please be comprehensive, and format for human readability by using smaller paragraphs."
    prompt = f"{instruction}\n\ncontext:\n{context_joined}\n\nquestion:\n{query}\n\nanswer:\n"
    print(prompt)

    response = get_completion(prompt, temperature=0.0, max_tokens=None)
    print(response)


if __name__ == '__main__':
    main(to_index=False)
