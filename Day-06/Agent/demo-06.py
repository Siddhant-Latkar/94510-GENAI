from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call

@wrap_model_call
def model_logging(request,handler):
    print("before model call:",'-'*20)
    #print(request)
    response=handler(request)
    print("After model call:",'-'*20)
    #print(response)
    response.result[0].content=response.result[0].content.upper()
    return response

@wrap_model_call
def limit_model_contex(request,handler):
    print("*Before model call :",'-' * 20)
    #print(request)
    request.messages=request.messages[-5:]
    response=handler(request)
    print("* After model call:", '-' * 20)
    #print(response)
    response.result[0].content = response.result[0].content.upper()
    return response

#create model
llm=init_chat_model(
    model="meta-llama-3.1-8b-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummykey"
)

#conversation
conversation=[]

#create agent
agent=create_agent(model= llm,tools=[],middleware=[model_logging,limit_model_contex],system_prompt="You are helpful assistant.Answer in short but accurate")

while True:
    user_input=input("Ask:-")

    if user_input == "exit":
        break

    conversation.append({"role":"user","content": user_input})
    #invoke the agent
    result = agent.invoke ({"messages": conversation})
    #print the result's last message
    ai_msg=result["messages"][-1]

    print("AI:-",ai_msg.content)
    # let's use conversation history returned by agent
    conversation=result["messages"]
