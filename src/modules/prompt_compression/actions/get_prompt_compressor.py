from llmlingua import PromptCompressor

llm_lingua = PromptCompressor(
    # model_name = "NousResearch/Llama-2-7b-hf",
    model_name = "4bit/Llama-2-7b-chat-hf",
    device_map = "cpu",
    use_auth_token = False,
    open_api_config = {}, 
)

# llm_lingua = PromptCompressor(
#     model_name="NousResearch/Llama-2-7b-hf",
#     device_map="cpu",
#     use_auth_token=False,
#     open_api_config={},
# )
