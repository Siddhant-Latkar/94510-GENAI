import os 
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()
api_key="dummy-key"
url="http://127.0.0.1:1234/v1/chat/completions"

headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

while True:
    User_prompt=input("Ask Anything=")
    if User_prompt=="exit":
        break

    req_data={
        "model" :"meta-llama-3.1-8b-instruct",
        "messages" :[{"role":"user","content":User_prompt}]
    }

    time_1=time.perf_counter()
    response=requests.post(url,data=json.dumps(req_data),headers=headers)
    res=response.json()
    time_2=time.perf_counter()
    #print(res)
    print(res["choices"][0]["message"]["content"])
    print("time require=",time_2-time_1)