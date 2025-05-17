# 🛍️ GenAI E-Commerce Product Search (Production Version)

This project is a production-ready implementation of a **GenAI-powered product search system** using **web scraping**, **semantic embeddings**, **FAISS vector search**, and **natural language generation**.

## 🔍 Features

- ✅ Scrapes product data (e.g. laptops) from a sample website  
- 🧠 Converts product descriptions into dense embeddings  
- 📦 Stores searchable vectors in a FAISS index  
- 🔎 Supports semantic search using natural language queries  
- 🧾 Generates user-friendly summaries of search results  


genai_ecommerce/
├── data/
│   ├── faiss_index.index     # FAISS index file
│   └── products.pkl          # Pickled product metadata
├── modules/
│   ├── embed.py              # Scraping, embedding, and FAISS indexing
│   ├── search.py             # Query embedding and similarity search
│   └── generate.py           # LLM-based natural language generation
├── main.py                   # Orchestration script to run the full pipeline
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

 Dependencies
beautifulsoup4, requests – Web scraping

sentence-transformers – Embedding product data

faiss-cpu – Vector storage and similarity search

transformers / openai – LLM-based recommendation generation

pickle, pandas, argparse – Utility functions

How It Works
Scrape: embed.py scrapes product data like title, specs, price.

Embed: Each product description is converted to a vector via a transformer model.

Store: These vectors are saved in a FAISS index, along with raw product info.

Search: search.py embeds user queries and retrieves top-k similar items.

Generate: generate.py summarizes results using GPT-like models.

 Example Output
Query: "Best lightweight laptop for students under 40K"

Response:

“We found 3 great options for you! 🎓 The Lenovo IdeaPad Slim 3 offers 8GB RAM and SSD storage under ₹39,999, ideal for portability. The HP 15s balances performance and price, while the Acer Aspire 3 includes a backlit keyboard and fast charging.”

 API or UI (Optional Extension)
You can later wrap this into a FastAPI/Streamlit app:

/search?query=... → Returns list of recommended products

/recommend → Returns generated summaries

 Roadmap
 Laptop product search

 Multi-category product support (phones, appliances)

 Multilingual search

 LLM agents to refine queries

 Web app interface (FastAPI/Streamlit)

 User profile-based recommendations






