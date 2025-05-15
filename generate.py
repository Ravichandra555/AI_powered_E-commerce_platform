# generate.py

def generate_response(query, results):
    resp = f"You asked for: {query}\nHere are top {len(results)} matches:\n"
    for idx, prod in enumerate(results, 1):
        resp += f"{idx}. {prod}\n"
    return resp

if __name__ == "__main__":
    sample_query   = "office laptop under $500"
    sample_results = [
        "Lenovo IdeaPad — $499: Basic office laptop",
        "HP 15 — $479: 8GB RAM, 256GB SSD"
    ]
    print(generate_response(sample_query, sample_results))
