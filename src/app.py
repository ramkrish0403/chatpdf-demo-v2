import sys
from pathlib import Path

from requests import get

# Add the top-level folder of the project to sys.path
top_level_dir = str(Path(__file__).resolve().parent.parent)
if top_level_dir not in sys.path:
    sys.path.append(top_level_dir)


import os
from modules.extractors.index import extractPDF
from modules.chunking.index import chunk_text
from modules.indexing.index import index_chunks
from modules.context.index import get_context
from modules.prompt_compression.index import get_longLLMLingua_compressed_prompt


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
    query = "What is the termination policy?"
    context = get_context(query)
    print(context)

    # Get the compressed prompt
    compressed_prompt = get_longLLMLingua_compressed_prompt(
        context=context,
        query=query,
        instruction="Answer the question based on the context retrieved from the employee handbook."
    )
    print(compressed_prompt)



if __name__ == '__main__':
    main(to_index=False)
