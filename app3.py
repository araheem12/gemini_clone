# app.py
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    google_api_key="AIzaSyDJQC1tWpupjjAhc6d7CqkA8u1j3V3WTKg",
    temperature=0.7
)

# Set up Streamlit page
st.set_page_config(page_title="🤖 Gemini Chat Clone", page_icon="🌟")
st.title("🌟 Gemini Chat Clone")

# Initialize session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("ai").markdown(msg.content)

# Input prompt from user
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Show user's message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Get response from Gemini
    with st.chat_message("ai"):
        with st.spinner("Gemini is thinking..."):
            try:
                response = llm.invoke(st.session_state.messages)
                st.markdown(response.content)
                st.session_state.messages.append(AIMessage(content=response.content))
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
