import streamlit as st

st.title("⚙️ Admin & Settings")

st.checkbox("Enable Hybrid NLP+Rules extraction", value=True)
st.checkbox("Enable LLM-only extraction", value=False)
st.checkbox("Auto-refresh embeddings for GraphRAG", value=True)

st.markdown("---")
st.subheader("Export Data")
col1, col2, col3 = st.columns(3)
col1.button("Export CSV")
col2.button("Export JSON")
col3.button("Export Neo4j Cypher")

st.info("Future: user authentication, role-based access, audit logs")
