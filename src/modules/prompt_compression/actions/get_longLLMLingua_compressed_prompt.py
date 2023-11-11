from ast import List
from .get_prompt_compressor import llm_lingua


def get_longLLMLingua_compressed_prompt(context: List[str], query: str, instruction: str):
    response = llm_lingua.compress_prompt(
        context=context,
        instruction=instruction,
        question=query,
        rank_method="longllmlingua"
    )
    print(response)
    compressed_prompt = response['compressed_prompt']
    return compressed_prompt
