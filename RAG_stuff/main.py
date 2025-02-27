import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from play_ground import play_ground

# Load env files
load_dotenv()

user_promt = "What are the six fields of action in Siemens' DEGREE Sustainability Framework, and how do they guide responsible business practices?"

# Directly assigning values (ensure these are securely managed in production)
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYED_NAME")

#cognitiveServicesResource = os.getenv("AZURE_SEARCH_SERVICE_NAME")
azure_search_endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
azure_search_index = os.getenv("AZURE_AI_SEARCH_INDEX")
azure_search_api_key = os.getenv("AZURE_SEARCH_API_KEY")

# Initialize Azure OpenAI client with Entra ID authentication
token_provider = get_bearer_token_provider(
     DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)
client = AzureOpenAI(
    azure_endpoint = endpoint,
    azure_ad_token_provider = token_provider,
    api_version = "2024-05-01-preview"
)

play_ground(client,deployment,user_promt,azure_search_endpoint,azure_search_index,azure_search_api_key)