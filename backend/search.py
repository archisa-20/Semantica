from sentence_transformers import SentenceTransformer
import numpy as np
from backend.data import movies

# Load the model (downloads once, ~80MB)
print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Extract all descriptions and encode them into vectors
descriptions = [m["description"] for m in movies]
print("Embedding movie descriptions...")
embeddings = model.encode(descriptions)  # shape: (20, 384)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query, top_k=3):
    query_embedding = model.encode(query)
    scores = [cosine_similarity(query_embedding, emb) for emb in embeddings]
    top_indices = np.argsort(scores)[::-1][:top_k]

    print(f"\n🔍 Results for: '{query}'\n" + "-" * 40)
    for rank, idx in enumerate(top_indices, 1):
        print(f"{rank}. {movies[idx]['title']}  (score: {scores[idx]:.4f})")
        print(f"   {movies[idx]['description']}\n")

# Interactive search loop
print("\n✅ Ready! Type anything to search. ('quit' to exit)\n")
while True:
    query = input("Search: ").strip()
    if query.lower() in ("quit", "exit", "q"):
        break
    if query:
        search(query)
        