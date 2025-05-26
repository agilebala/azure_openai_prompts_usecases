from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    policy = input("Paste company policy or knowledge base excerpt:\n")
    question = input("Enter your question:\n")
    messages = [
        {"role": "system", "content": "Answer the user's question using only the provided company policy."},
        {"role": "user", "content": f"Policy: {policy}\nQuestion: {question}"}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
