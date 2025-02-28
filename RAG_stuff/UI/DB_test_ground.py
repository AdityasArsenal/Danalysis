from pymongo import MongoClient
import uuid
from datetime import datetime

# Connection string and database/collection setup
connection_string = "mongodb://chat-history-with-cosmos:aWQkNybTHAZ4ZHgYXGNb4E2VDQ2BGP8k0WYyGPuziM4D5TayG2Pf5fnxFSD8Y3nI6wmXJvph3In1ACDbKj2jRQ==@chat-history-with-cosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@chat-history-with-cosmos@"
client = MongoClient(connection_string)
db = client["ChatHistoryDtabse"]
collection = db["chat-history-with-cosmos"]

# Insert a sample document
sample_doc = {
    "id": "67c13b069d3346d68c93a4fy",
    "user_prompt": "Hello, how are you ",
    "model_response": "fuck you",
    "timestamp": datetime.utcnow().isoformat(),
    "references": "3"
}
collection.insert_one(sample_doc)
print("Document inserted:", sample_doc)

chat_history_retrival_limit = 10

chat_history_retrieved = list(collection.find({"id": "67c13b069d3346d68c93a4fy"}))

recent_chat_history = chat_history_retrieved[-chat_history_retrival_limit:] if chat_history_retrieved else []

provided_conversation_history = []
for doc in recent_chat_history:
    user_message = doc.get("user_prompt", "")
    ai_message = doc.get("model_response", "")
    provided_conversation_history.append({"Me": user_message})
    provided_conversation_history.append({"Your response": ai_message})

print(f"retriveed docs : {provided_conversation_history}")