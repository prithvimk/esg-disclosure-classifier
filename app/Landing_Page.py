import streamlit as st

st.set_page_config(page_title="ESG Knowledge Graph", layout="wide")

st.title("🌍 ESG Knowledge Graph Dashboard")

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Entities", "1523")
col2.metric("Companies", "432")
col3.metric("Regulations", "56")

col4, col5 = st.columns(2)
col4.metric("Relationships", "8902")
col5.metric("Countries", "28")

st.markdown("---")
st.subheader("Highlights")
st.write("• Top 5 Companies by CO₂ Reduction")  
st.write("• Most Cited Regulation: EU Taxonomy")  
st.write("• Sectors with highest ESG mentions")  

st.info("➡️ Use the sidebar to explore Graph, Documents, Analytics, and Admin pages.")
