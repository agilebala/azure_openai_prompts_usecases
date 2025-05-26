import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env
load_dotenv()

def get_openai_client():
    """
    Returns an AzureOpenAI client using API key authentication.
    """
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")

    if not endpoint or not api_key:
        raise ValueError("Both AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set in your .env file.")

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version
    )
    return client

def get_deployment_name():
    return os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")

def get_max_tokens():
    return int(os.getenv("AZURE_OPENAI_MAX_TOKENS", "256"))

def get_temperature():
    return float(os.getenv("AZURE_OPENAI_TEMPERATURE", "0.2"))

