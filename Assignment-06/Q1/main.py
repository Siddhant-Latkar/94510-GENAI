import streamlit as st
from dotenv import load_dotenv
import json
import requests
import os

st.title("--AI Chatbot--")
with st.sidebar:
    st.header("Select")
    model=st.selectbox("Select",["Groq","LM-Studio"])


load_dotenv()
#sesssion state
if "messases" not in st.session_state:
    st.session_state.messages=[]

#for  showng chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

Groq_api=os.getenv("GROQ_API_KEY")
LM_api="dummy key"

#------Groq---------
Groq_url="https://api.groq.com/openai/v1/chat/completions"

Cloud_headers={
    "Authorization": f"Bearer {Groq_api}",
    "Content-type": "application/json"
}


if model=="Groq":

    user_input=st.chat_input("Ask anything:-")
    if user_input:
        st.session_state.messages.append({
            "role":"user",
            "content":user_input
        })
        req_data={
            "model":"llama-3.3-70b-versatile",
            "messages": st.session_state.messages

        }

        response=requests.post(
            Groq_url,
            headers=Cloud_headers,
            json=req_data
        )

        #status code checking
        if response.status_code !=200:
            st.error(f"HTTP ERROR {response.status_code}")
        else:
            res=response.json()
            assistant_reply=res["choices"][0]["message"]["content"]
            st.session_state.message.append({
                "role":"assistant",
                "content": assistant_reply
            })

        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

# ------ LM-Studio -------
LM_url = "http://127.0.0.1:1234/v1/chat/completions"

LM_Headers = {
    "Authorization": "Bearer dummy",
    "Content-Type": "application/json"
}

if model == "LM-Studio":
    user_prompt = st.chat_input("Ask anything:-")

    if user_prompt:
        st.session_state.messages.append({
            "role": "user",
            "content": user_prompt
        })
        req_data = {
            "model": "meta-llama-3.1-8b-instruct",
            "messages": st.session_state.messages
            
        }

        response = requests.post(
            LM_url,
            headers=LM_Headers,
            json=req_data
        )

        if response.status_code != 200:
            st.error(f"HTTP ERROR {response.status_code}")
        else:
            res = response.json()
            assistant_reply=res["choices"][0]["message"]["content"]

            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_reply
            }
            )

            with st.chat_message("assistant"):
                st.markdown(assistant_reply)
            

