from utils.openai_client import get_openai_client,get_deployment_name,get_max_tokens,get_temperature
def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    messages = [
        {"role": "system","content": "You are a helpful support agent. Answer user questions clearly and escalate if you cannot resolve."},
        {"role": "user","content": "My order hasn't arrived. Can you check the status?"}
    ]
    response = client.chat.completions(
        model = deployment,
        messages = messages,
        max_token = get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)