import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

# Azure OpenAI setup
api_key = os.getenv('AZURE_OPENAI_API_KEY')
api_version = os.getenv('AZURE_OPENAI_API_VERSION_E')
azure_openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
azure_openai_deployed_name = os.getenv('AZURE_OPENAI_DEPLOYED_NAME_E')

client = AzureOpenAI(
    api_key = api_key,
    api_version = api_version,
    azure_endpoint = azure_openai_endpoint
)

# Create an embedding for the query
query = "What is the annual income?"
embedding_response = client.embeddings.create(
    model=azure_openai_deployed_name,
    input=query
)

# Fetch and print only the embeddings
embeddings = [item.embedding for item in embedding_response.data]
#print(embeddings)
