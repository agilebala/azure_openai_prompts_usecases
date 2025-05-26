from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

from openai import AzureOpenAI

# Optional: Azure AD authentication (recommended for production)
try:
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    USE_AZURE_AD = True
except ImportError:
    USE_AZURE_AD = False

def get_openai_client():
    """
    Returns an AzureOpenAI client using either API key or Azure AD token provider.
    """
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")

    if USE_AZURE_AD and not api_key:
        # Use Azure AD (Managed Identity or Service Principal)
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://cognitiveservices.azure.com/.default"
        )
        client = AzureOpenAI(
            azure_endpoint=endpoint,
            azure_ad_token_provider=token_provider,
            api_version=api_version
        )
    else:
        # Use API key (default for development)
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
