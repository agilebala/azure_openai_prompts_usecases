from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    manual = input("Paste manual or documentation text:\n")
    query = input("Describe the issue or information you are searching for:\n")
    messages = [
        {"role": "system", "content": "Find the most relevant section in the following manual for the user's query."},
        {"role": "user", "content": f"Manual: {manual}\nQuery: {query}"}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
