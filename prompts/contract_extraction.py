from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    contract_text = input("Paste contract text:\n")
    messages = [
        {"role": "system", "content": "Extract parties, contract date, and payment terms from the following contract."},
        {"role": "user", "content": contract_text}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
