
import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


# Initialize Azure OpenAI client with Entra ID authentication
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), powershell -ex AllSigned -c "Invoke-RestMethod 'https://aka.ms/install-azd.ps1' | Invoke-Expression"
VERBOSE: Downloading build from https://azd-release-gfgac2cmf7b8cuay.b02.azurefd.net/azd/standalone/release/stable/azd-windows-amd64.msi
    f'{cognitiveServicesResource}.default'
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version='2024-05-01-preview',
)

completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant that helps people find information."
        }
    ],
    #past_messages=10,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    extra_body={
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": azure_search_endpoint,
                    "index_name": azure_search_index,
                    "authentication": {
                        "type": "api_key",
                        "api_key": azure_search_key
                    }
                }
            }
        ]
    }
)

print(completion.model_dump_json(indent=2))
