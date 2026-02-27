import requests
import numpy as np
from typing import List

API_URL = "http://localhost:8000/embed"   # your FastAPI endpoint


def get_embedding(text: str) -> List[float]:
    response = requests.post(API_URL, json={"text": text})
    response.raise_for_status()
    return response.json()["embedding"]


def cosine_similarity(a: List[float], b: List[float]) -> float:
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# ---- Example usage ----

A = "blond"
B = "black"
C = "brown"
D = "yellow hair"

# Get embeddings
emb_A = get_embedding(A)
emb_B = get_embedding(B)
emb_C = get_embedding(C)
emb_D = get_embedding(D)

# Compute similarities
scores = {
    "A": cosine_similarity(emb_A, emb_D),
    "B": cosine_similarity(emb_B, emb_D),
    "C": cosine_similarity(emb_C, emb_D),
}

# Find the best match
most_similar = max(scores, key=scores.get)

print("Similarity scores:", scores)
print("Most similar to D:", most_similar)
