# pages/02_data_visualization.py
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection


st.set_page_config(
    page_title="Data | Escape Streamlit App",
    page_icon="📊",
)

conn = st.connection("gsheets", type=GSheetsConnection)

df_priority = conn.read(
    worksheet=2085186136,
    ttl="30m",
)

st.title('Data Visualization')
st.markdown("""
You can select the priority and demo booked status to filter the data. The filtered data is displayed in the table below.
""")


def format_data(df):
    for col in ['Visited Website', 'Demo Booked', 'Demo Done', 'Meeting Planned', 'POC Started']:
        df[col] = df[col] == 'Yes'


format_data(df_priority)

# Filters
priority_filter = st.sidebar.multiselect('Priority', sorted(df_priority['Priority'].unique()))
demo_filter = st.sidebar.multiselect('Demo Booked', sorted(df_priority['Demo Booked'].unique()))

# Filtered DataFrame
df_filtered = df_priority[df_priority["Priority"].isin(priority_filter) & df_priority['Demo Booked'].isin(demo_filter)]

st.dataframe(df_filtered)
