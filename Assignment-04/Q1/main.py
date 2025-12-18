import streamlit as st 
import time 

st.set_page_config(page_title="Chat_Bot",layout="centered")
st.title("My Chat Bot")

if "message" not in st.session_state:
    st.session_state.message=[] 

#for msg in st.session_state.message:
    #with st.chat_message(msg["role"]):
        #st.markdown(msg["content"])

if st.session_state.message:
    st.subheader("Chat History")
    for msg in st.session_state.message:
        st.write(msg)

user_input=st.chat_input("Type Your Message")

def stream_reply(text, delay=0.05):
    """Generator for streaming text with delay"""
    for char in text:
        yield char
        time.sleep(delay)

if user_input:
    st.session_state.message.append(user_input)

with st.chat_message("user"):
        st.markdown(user_input)

    
bot_reply = f"You said: {user_input}"

    
with st.chat_message("assistant"):
    streamed_text = st.write_stream(
        stream_reply(bot_reply)
    )