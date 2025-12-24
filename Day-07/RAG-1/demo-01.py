from sentence_transformers import SentenceTransformer
import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))


embed_model=SentenceTransformer("all-miniLM-L6-v2")

sentence=[
    "I love cricket",
    "cricket is very intresting game",
    "india won their 1st cricket world cup in 1983"
]

emebeddings=embed_model.encode(sentence)

for embed_vect in emebeddings:
    print("Len:",len(embed_vect),"--->",embed_vect[:4])

print("Sentence 1 & 2 similarity: ", cosine_similarity(emebeddings[0],emebeddings[1]))
print("Sentence 1 & 3 similarity: ", cosine_similarity(emebeddings[0],emebeddings[2]))
print("Sentence 2 & 3 similarity: ", cosine_similarity(emebeddings[1],emebeddings[2]))

