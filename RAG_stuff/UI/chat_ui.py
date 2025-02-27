import streamlit as st
import requests

# Backend URL
WEBHOOK_URL = "http://localhost:8000/chat"

# Initialize session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("AI Chat Interface")

def display_chat():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Display chat history
display_chat()

# Get user input
user_input = st.chat_input("Enter your message here")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Send request to FastAPI
    payload = {"user_prompt": user_input}
    
    with st.spinner("AI is thinking..."):
        response = requests.post(WEBHOOK_URL, json=payload)
    
    if response.status_code == 200:
        ai_message = response.json().get("response", "Sorry, no response was generated.")
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
    
    st.rerun()
