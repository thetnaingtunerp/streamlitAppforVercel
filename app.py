import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Streamlit Plotly App", layout="wide")

st.title("📊 Streamlit App with Plotly")

# Sample data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 150, 90, 180, 210],
    "Profit": [30, 45, 20, 60, 75]
})

st.subheader("Raw Data")
st.dataframe(df)

# Plotly line chart
fig = px.line(
    df,
    x="Month",
    y=["Sales", "Profit"],
    markers=True,
    title="Sales & Profit Trend"
)

st.plotly_chart(fig, use_container_width=True)
