import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import requests

# Azure Cognitive Search setup
search_service_name = os.getenv('AZURE_SEARCH_SERVICE_NAME')
search_index_name = os.getenv('AZURE_SEARCH_INDEX_NAME')
search_api_key = os.getenv('AZURE_SEARCH_API_KEY')

# Construct the search endpoint
search_endpoint = f"https://{search_service_name}.search.windows.net/indexes/{search_index_name}/docs/search?api-version=2021-04-30-Preview"

# Construct the search payload
search_payload = {
    "search": query,  # Pass the query directly
    "top": 5,  # Number of search results to return
    "queryType": "hybride",  # Use semantic query syntax
    "queryLanguage": "en-us",  # Specify the query language
}

# Set the headers for the search request
headers = {
    "Content-Type": "application/json",
    "api-key": search_api_key
}

# Send the search request to Azure Cognitive Search
response = requests.post(search_endpoint, json=search_payload, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    search_results = response.json()
    # Extract and print only the chunk values
    chunks = [doc['chunk'] for doc in search_results['value']]
    for chunk in chunks:
        print(chunk)
else:
    print(f"Error: {response.status_code} - {response.text}")

# Questions:
# 1. Is the API version for Azure Cognitive Search correct? (Assumed "2021-04-30-Preview" here)
# 2. How many search results should be returned? (Assumed "top": 5 here)
# 3. Is the semantic configuration name "hybrid" correct? (Assumed "hybrid" here)

