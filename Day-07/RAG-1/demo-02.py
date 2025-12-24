from langchain_openai import OpenAIEmbeddings

import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)* np.linalg.norm(b))

embed_model=OpenAIEmbeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    base_url="http://localhost:1234/v1",
    api_key="dummykey",
    check_embedding_ctx_length=False
)

sentence=[
    "I love cricket",
    "cricket is very intresting game",
    "india won their 1st cricket world cup in 1983"
]

emebeddings=embed_model.embed_documents(sentence)

for embed_vect in emebeddings:
    print("Len:",len(embed_vect),"--->",embed_vect[:4])

print("Sentence 1 & 2 similarity: ", cosine_similarity(emebeddings[0],emebeddings[1]))
print("Sentence 1 & 3 similarity: ", cosine_similarity(emebeddings[0],emebeddings[2]))
print("Sentence 2 & 3 similarity: ", cosine_similarity(emebeddings[1],emebeddings[2]))


