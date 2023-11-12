from src.modules.openai.index import get_completion

def get_hypothetical_response(query: str):
    instruction = "We want to retrieve context from the employee handbook. Please generate hypothetical response, which we will use to extract the context from the handbook. Please generate keeping in mind the possible variations."
    prompt = f"{instruction}\nuser question:{query}\nhypothetical answer:"
    # print(prompt)

    response = get_completion(prompt)
    print("hypothetical response: ", response)
    return response