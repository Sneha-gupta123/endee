import pandas as pd
from embeddings import create_embedding
from endee import EndeeClient

# Initialize Endee client
client = EndeeClient()

# Create collection
collection = client.create_collection(
    name="grocery_products",
    dimension=384
)

# Load dataset
data = pd.read_csv("dataset/products.csv")

# Combine product + description
data["text"] = data["product"] + " " + data["description"]

# Insert vectors into Endee
for i, row in data.iterrows():

    vector = create_embedding(row["text"])

    collection.insert({
        "id": str(i),
        "vector": vector,
        "metadata": {
            "product": row["product"],
            "category": row["category"],
            "price": row["price"],
            "store": row["store"]
        }
    })

# Search function
def search_products(query):

    query_vector = create_embedding(query)

    results = collection.search(
        vector=query_vector,
        top_k=5
    )

    return results