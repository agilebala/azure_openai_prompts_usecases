from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    data = input("Paste quarterly sales or business data:\n")
    messages = [
        {"role": "system", "content": "Generate an executive summary from the following business data."},
        {"role": "user", "content": data}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
