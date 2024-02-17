# app.py
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Page Configuration
st.set_page_config(
    page_title="Escape Streamlit App",
    page_icon="📊",
)
# Google Sheets Connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Assuming these IDs or names need to be adjusted based on your Google Sheets setup
df_priority = conn.read(
    worksheet=2085186136,
    ttl="30m",
)
df_raw = conn.read(
    ttl="30m",
)


st.title('Welcome to the Lead Funnel Analysis App 📊')
st.markdown("""
This app provides insights into the sales funnel, highlighting areas for improvement and showcasing key performance indicators (KPIs) for leads processing.
- **Navigate through the sidebar** to access different analyses and visualizations.
- Explore **Funnel Visualization**, **Data Visualization**, and **KPI Analysis** to gain insights into lead management effectiveness.

""")

st.write("---")
st.write("Streamlit App by Leonard Roussard")