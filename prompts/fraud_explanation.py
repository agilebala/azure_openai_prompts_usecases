from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    txn_details = input("Paste transaction details:\n")
    messages = [
        {"role": "system", "content": "Explain in plain language why the following transaction was flagged as potentially fraudulent."},
        {"role": "user", "content": txn_details}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
