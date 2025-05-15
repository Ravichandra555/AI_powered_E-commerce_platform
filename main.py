# main.py

import embed
from search import ProductSearch
from generate import generate_response

def main():
    # Step 1: Scrape & embed (run once; comment out after the first successful run)
    print("=== Embedding phase ===")
    products = embed.scrape_test_site()
    if not products:
        print("No products scraped. Exiting.")
        return
    embed.embed_and_save(products)

    # Step 2: Initialize search
    print("\n=== Search phase ===")
    ps = ProductSearch()

    # Step 3: Interactive loop
    while True:
        query = input("\nEnter search query (or 'exit'): ").strip()
        if query.lower() in ('exit', 'quit'):
            break
        results = ps.search(query)
        response = generate_response(query, results)
        print("\n" + response)

    print("Goodbye!")

if __name__ == "__main__":
    main()

