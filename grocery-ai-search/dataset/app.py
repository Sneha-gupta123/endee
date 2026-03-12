import streamlit as st
from vector_search import search_products

st.title("Town Grocery AI Search")

query = st.text_input("Search grocery items")

if query:

    results = search_products(query)

    for r in results:

        product = r["metadata"]["product"]
        category = r["metadata"]["category"]
        price = r["metadata"]["price"]
        store = r["metadata"]["store"]

        st.write("Product:", product)
        st.write("Category:", category)
        st.write("Price:", price)
        st.write("Store:", store)
        st.write("---")