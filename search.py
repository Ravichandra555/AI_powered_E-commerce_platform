# search.py

import faiss
import pickle
from sentence_transformers import SentenceTransformer

INDEX_PATH = "faiss_index.index"
DATA_PATH  = "products.pkl"

class ProductSearch:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        print("Loading index & products…")
        self.index    = faiss.read_index(INDEX_PATH)
        with open(DATA_PATH, "rb") as f:
            self.products = pickle.load(f)
        self.model    = SentenceTransformer(model_name)

    def search(self, query, top_k=5):
        print(f"Searching for: {query!r}")
        qv = self.model.encode([query]).astype("float32")
        D, I = self.index.search(qv, top_k)
        return [self.products[i] for i in I[0]]

if __name__ == "__main__":
    ps = ProductSearch()
    results = ps.search("budget laptop with i5")
    print("\nTop results:")
    for i, prod in enumerate(results, 1):
        print(f"{i}. {prod}")
