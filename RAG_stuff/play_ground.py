import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

# Load env files
load_dotenv()

# Directly assigning values (ensure these are securely managed in production)
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYED_NAME")

cognitiveServicesResource = os.getenv("AZURE_SEARCH_SERVICE_NAME")
azure_search_endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
azure_search_index = os.getenv("AZURE_AI_SEARCH_INDEX")
azure_search_key = os.getenv("AZURE_SEARCH_API_KEY")

# Initialize Azure OpenAI client with Entra ID authentication
token_provider = get_bearer_token_provider(
     DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version='2024-05-01-preview',
)

completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps people find information, from the source provided"},
        {"role": "user", "content": "Hello, What are the six fields of action in Siemens' DEGREE Sustainability Framework, and how do they guide responsible business practices?"}
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
                        "key": azure_search_key
                    }
                }
            }
        ]
    }
)

print(completion.model_dump_json(indent=1))
