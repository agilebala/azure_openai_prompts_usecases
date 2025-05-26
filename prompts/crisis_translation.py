from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    message = input("Paste emergency message (any language):\n")
    messages = [
        {"role": "system", "content": "Translate this emergency message to English and summarize the main action required."},
        {"role": "user", "content": message}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
