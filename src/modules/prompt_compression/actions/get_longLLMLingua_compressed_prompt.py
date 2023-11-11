from ast import List
from .get_prompt_compressor import llm_lingua


def get_longLLMLingua_compressed_prompt(context: List[str], query: str, instruction: str):
    response = llm_lingua.compress_prompt(
        context=context,
        instruction=instruction,
        question=query,
        ratio=0.75,  # for 4x speedup
        iterative_size=200,
        condition_compare=True,
        condition_in_question='after_condition',
        rank_method='longllmlingua',
        reorder_context='sort',
        dynamic_context_compression_ratio=0.3,
        context_budget="+200",
    )
    print(response)
    compressed_prompt = response['compressed_prompt']
    return compressed_prompt
