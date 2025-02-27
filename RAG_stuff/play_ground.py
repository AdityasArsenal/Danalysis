
import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Directly assigning values (ensure these are securely managed in production)
endpoint = "https://opeanai-servicies.openai.azure.com/openai/deployments/gpt-4o/extensions/chat/completions?api-version=2024-02-15-preview"
deployment = "gpt-4o"
cognitiveServicesResource = "aisearchservicee"
azure_search_endpoint = "https://aisearchservicee.search.windows.net"
azure_search_index = "vectorization-open-ada"
azure_search_key = "2Bz4dmBVw8zZZ4IzEZ08n5w1YdDu65x1dsX3WpBAgyAzSeCZwpbC"

# Initialize Azure OpenAI client with Entra ID authentication
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
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
