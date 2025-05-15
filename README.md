# 🛍️ GenAI E-Commerce Product Search (Production Version)

This project is a production-ready implementation of a **GenAI-powered product search system** using **web scraping**, **semantic embeddings**, **FAISS vector search**, and **natural language generation**.

## 🔍 Features

- ✅ Scrapes product data (e.g. laptops) from a sample website  
- 🧠 Converts product descriptions into dense embeddings  
- 📦 Stores searchable vectors in a FAISS index  
- 🔎 Supports semantic search using natural language queries  
- 🧾 Generates user-friendly summaries of search results  

## 🗂️ Folder Structure

├── embed.py # Scrapes products, embeds them, builds FAISS index
├── search.py # Searches for user queries using semantic similarity
├── generate.py # Generates natural language recommendations
├── main.py # Main controller (can call all steps)
├── requirements.txt
├── faiss_index.index
├── products.pkl
└── README.md


