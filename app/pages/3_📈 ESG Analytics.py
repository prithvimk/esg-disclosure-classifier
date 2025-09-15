import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 ESG Analytics")

# Dummy dataset
df = pd.DataFrame({
    "Year": [2021, 2022, 2023],
    "CO₂ Emissions (tons)": [1200, 1100, 950],
    "Company": ["ABC Corp"] * 3
})

company = st.selectbox("Select Company", df["Company"].unique())
metric = st.selectbox("Metric", ["CO₂ Emissions (tons)", "Gender Diversity (%)"])

fig = px.line(df, x="Year", y=metric, color="Company", title=f"{metric} Trend")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Comparison")
col1, col2 = st.columns(2)
col1.write("Company A: CO₂ ↓ 15%")  
col2.write("Company B: CO₂ ↑ 5%")
