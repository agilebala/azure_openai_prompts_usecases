from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    product = input("Describe your product or campaign:\n")
    messages = [
        {"role": "system", "content": "Write a catchy LinkedIn post announcing our new product or campaign."},
        {"role": "user", "content": product}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
