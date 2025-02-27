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

