import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('AZURE_OPENAI_API_KEY')
api_version = os.getenv('AZURE_OPENAI_API_VERSION')
azure_openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
azure_openai_deployed_name = os.getenv('AZURE_OPENAI_DEPLOYED_NAME')

client = AzureOpenAI(
    api_key = api_key,
    api_version = api_version,
    azure_endpoint = azure_openai_endpoint
)

response = client.chat.completions.create(
    model= azure_openai_deployed_name,
    messages=[
        {
            "role": "user",
            "content": "tell me a joke"
        }
    ]
)

print(response.choices[0].message.content)
