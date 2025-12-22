from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

llm= init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

conversation=[
    {"role":"system","content": "You are a helpful assistant"}
]
k=int(input("enter k value="))

while True:
    user_input=input("You:-")
    if user_input== "exit":
        break

    user_msg={"role":"user","content": user_input}
    conversation.append(user_msg)
    
    # Use slider value to decide how many last messages to be sent to LLM
    # instead of full conversation. This will limit the "context length".
    #--->
    system_msg= conversation[0]
    recent_msgs = conversation[-k * 2:]
    context=[system_msg] + recent_msgs

    llm_output =llm.invoke(conversation)
    print("AI:-",llm_output.content)
    llm_msg={"role":"assistant","content": llm_output.content}
    conversation.append(llm_msg)

    
