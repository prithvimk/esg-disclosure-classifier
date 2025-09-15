import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("🌐 Knowledge Graph Explorer")

st.sidebar.subheader("Filters")
company = st.sidebar.selectbox("Select Company", ["All", "ABC Corp", "XYZ Energy"])
esg_type = st.sidebar.selectbox("ESG Category", ["All", "Environmental", "Social", "Governance"])
year = st.sidebar.selectbox("Year", ["All", "2023", "2022", "2021"])

st.markdown("### Graph Visualization")

# Fake example graph
G = nx.Graph()
G.add_node("ABC Corp", color="blue")
G.add_node("CO₂ Emissions", color="green")
G.add_edge("ABC Corp", "CO₂ Emissions")

fig, ax = plt.subplots()
nx.draw(G, with_labels=True, node_color="lightblue", node_size=3000, ax=ax)
st.pyplot(fig)

st.markdown("### Evidence Panel")
st.write("**ABC Corp reduced CO₂ emissions by 15% in 2024**")  
st.caption("Source: ABC Sustainability Report, p. 14")
