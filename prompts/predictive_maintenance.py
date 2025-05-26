from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    sensor_log = input("Paste sensor log data:\n")
    messages = [
        {"role": "system", "content": "Based on the following sensor log, predict if maintenance is required soon."},
        {"role": "user", "content": sensor_log}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
