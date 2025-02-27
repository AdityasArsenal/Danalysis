from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from play_ground import play_ground

# Load environment variables
load_dotenv()
app = FastAPI()

# Azure configuration
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYED_NAME")
azure_search_endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
azure_search_index = os.getenv("AZURE_AI_SEARCH_INDEX")
azure_search_api_key = os.getenv("AZURE_SEARCH_API_KEY")

# Token authentication for Azure OpenAI
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)
client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-05-01-preview",
)

# Request model
class ChatRequest(BaseModel):
    user_prompt: str

# API Endpoint to receive user input and return AI response
@app.post("/chat")
def chat(request: ChatRequest):
    model_response, reference_points = play_ground(
        client, deployment, request.user_prompt, azure_search_endpoint, azure_search_index, azure_search_api_key
    )
    return {"response": model_response, "references": reference_points}

