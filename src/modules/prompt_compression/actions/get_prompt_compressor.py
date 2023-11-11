from llmlingua import PromptCompressor

llm_lingua = PromptCompressor(
    model_name = "NousResearch/Llama-2-7b-hf",
    device_map = "cpu",
    use_auth_token = False,
    open_api_config = {}, 
)