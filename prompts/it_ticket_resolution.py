from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    issue = input("Describe the IT issue (e.g., error message, problem):\n")
    messages = [
        {"role": "system", "content": "Suggest steps to resolve the following IT issue."},
        {"role": "user", "content": issue}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
