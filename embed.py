# embed.py

import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import pickle

INDEX_PATH = "faiss_index.index"
DATA_PATH  = "products.pkl"
URL        = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

def scrape_test_site():
    print("Scraping test site…")
    res = requests.get(URL)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    products = []
    cards = soup.select("div.thumbnail")
    print(f"Found {len(cards)} product cards on page")
    for card in cards:
        title_el = card.select_one("a.title")
        price_el = card.select_one("h4.price")
        desc_el  = card.select_one("p.description")
        if title_el and price_el and desc_el:
            title = title_el.get_text(strip=True)
            price = price_el.get_text(strip=True)
            desc  = desc_el.get_text(strip=True)
            products.append(f"{title} — {price}: {desc}")

    print(f"✅ Scraped {len(products)} products")
    return products

def embed_and_save(products, model_name="all-MiniLM-L6-v2"):
    print("Loading embedding model…")
    model = SentenceTransformer(model_name)

    print(f"Embedding {len(products)} products…")
    embeddings = model.encode(products, show_progress_bar=True).astype("float32")

    dim = embeddings.shape[1]
    print(f"Building FAISS index (dim={dim})…")
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    print(f"Saving index → {INDEX_PATH}")
    faiss.write_index(index, INDEX_PATH)
    print(f"Saving products → {DATA_PATH}")
    with open(DATA_PATH, "wb") as f:
        pickle.dump(products, f)

    print("✅ embed.py done.")

if __name__ == "__main__":
    prods = scrape_test_site()
    if not prods:
        print("❌ No products scraped. Exiting.")
        exit(1)
    embed_and_save(prods)






