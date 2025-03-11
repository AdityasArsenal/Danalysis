from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, PartitionKey
import uuid
from datetime import datetime

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

def play_ground(     
client,
deployment,
user_promt,
azure_search_endpoint,
azure_search_index,
azure_search_api_key,
):   
    chunks = []
    response_message = ""
    completion = client.chat.completions.create(
        model = deployment,
        messages=[
            {"role": "system", "content": f"You are an AI assistant that helps people find information, from the source provided"},
            {"role": "user", "content": f"{user_promt}"}
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
                            "key": azure_search_api_key
                        }
                    }
                }
            ]
        }
    )

    # Extract and print only the response and context chunks
    response_message = completion.choices[0].message.content
    context_chunks = [citation['content'] for citation in completion.choices[0].message.context['citations']]
    
    print("Response:")
    print(response_message)
    print("\nContext Chunks:")
    for chunk in context_chunks:
        chunks.append(chunk)
    print(chunks)

    return response_message, context_chunks


# Request model
class ChatRequest(BaseModel):
    user_prompt: str

# API Endpoint to receive user input and return AI response
@app.post("/chat")
def chat(request: ChatRequest):

    model_response, reference_points = play_ground(client, deployment, request.user_prompt, azure_search_endpoint, azure_search_index,azure_search_api_key)

    # Create a unique ID for this conversation entry

    return {"response": model_response, "references": reference_points}


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
