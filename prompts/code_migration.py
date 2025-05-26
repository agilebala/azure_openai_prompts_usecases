from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    legacy_code = input("Paste legacy code (e.g., COBOL):\n")
    target_lang = input("Target language (e.g., Python, Java): ")
    messages = [
        {"role": "system", "content": f"Convert the following code to {target_lang}."},
        {"role": "user", "content": legacy_code}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
