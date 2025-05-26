from utils.openai_client import get_openai_client, get_deployment_name, get_max_tokens, get_temperature

def run():
    client = get_openai_client()
    deployment = get_deployment_name()
    transcript = input("Paste the meeting transcript:\n")
    messages = [
        {"role": "system", "content": "Summarize the following meeting transcript in bullet points."},
        {"role": "user", "content": transcript}
    ]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=get_max_tokens(),
        temperature=get_temperature()
    )
    print(response.choices[0].message.content)
