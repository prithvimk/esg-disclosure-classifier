import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("📂 Document Explorer")

uploaded_file = st.file_uploader("Upload ESG PDF Report", type=["pdf"])

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
    
    # Send the file to the FastAPI endpoint
    response = requests.post(f"{API_URL}/uploadfile/", files=files)
    
    if response.status_code == 200:
        try:
            st.success(f"File uploaded and processed: {response.json()['filename']}")
            st.write(response.json()['message'])
        except:
            st.error(f"Error processing file: {response.json().get('error', 'Unknown error')}")

    

    

st.markdown("---")
st.subheader("Processed Documents")
docs = [
    {"name": "ABC Corp Report 2024", "status": "✅", "facts": ["CO₂ ↓ 15%", "Complies with EU Taxonomy"]},
    {"name": "XYZ Energy Report 2023", "status": "⏳", "facts": []},
]

for doc in docs:
    st.write(f"{doc['status']} **{doc['name']}**")
    if doc["facts"]:
        st.write("Extracted Facts:")
        for f in doc["facts"]:
            st.write(" -", f)
