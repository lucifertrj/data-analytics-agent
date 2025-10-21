import streamlit as st
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import pandas as pd
import io
import matplotlib.pyplot as plt

import os
os.environ['GOOGLE_API_KEY'] = "<api-key>" # replace with your Gemini API key - aistudio.google.com

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'df' not in st.session_state:
    st.session_state.df = None
if 'agent' not in st.session_state:
    st.session_state.agent = None

st.title("Data Analytics Agent")

def process_question(question):
    if st.session_state.agent is not None:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("assistant"):
            response = st.session_state.agent.run(question)
            st.session_state.messages.append({"role": "assistant", "content": response})

uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    if st.session_state.df is None:
        st.session_state.df = pd.read_csv(uploaded_file)
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
        )
        st.session_state.agent = create_pandas_dataframe_agent(
            llm,
            st.session_state.df,
            verbose=True,
            agent_type="tool-calling",
            allow_dangerous_code=True,
            handle_parsing_errors=True
        )

    st.header("Data Preview")
    st.dataframe(st.session_state.df.head())
else:
    st.sidebar.info("Upload a CSV File to start conversation")

st.header("Chat with Data Analytics Agent")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What do you want to know?"):
    if st.session_state.agent is not None:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            with st.spinner("Thinking..."):
                response = st.session_state.agent.run(prompt)
                
                if 'plt' in locals() or 'plt' in globals():
                    buf = io.BytesIO()
                    plt.savefig(buf, format='png')
                    buf.seek(0)
                    st.image(buf)
                    plt.clf()
                
                message_placeholder.markdown(response)
            
        st.session_state.messages.append({"role": "assistant", "content": response})
