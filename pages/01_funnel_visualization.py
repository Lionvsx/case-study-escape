# pages/01_funnel_visualization.py
import streamlit as st
import plotly.express as px
import pandas as pd
from plotly import graph_objects as go
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Funnel | Escape Streamlit App",
    page_icon="📊",
)

st.title('Funnel Visualization')
st.markdown("""
You can select the dataframe to visualize using the sidebar. The funnel visualization showcases the lead conversion rates across different stages of the sales funnel.
""")

conn = st.connection("gsheets", type=GSheetsConnection)

# Assuming these IDs or names need to be adjusted based on your Google Sheets setup
df_raw = conn.read(
    ttl="30m",
)
df_priority = conn.read(
    worksheet=2085186136,
    ttl="30m",
)




def format_data(df):
    for col in ['Visited Website', 'Demo Booked', 'Demo Done', 'Meeting Planned', 'POC Started']:
        df[col] = df[col] == 'Yes'


format_data(df_raw)
format_data(df_priority)

selected_df = st.sidebar.selectbox('Select the dataframe', ('All data', 'Data without personal emails'))

funnel_steps = ['Visited Website', 'Demo Booked', 'Demo Done', 'Meeting Planned', 'POC Started']
funnel_counts = [df_raw[step].sum() for step in funnel_steps]

if selected_df == 'All data':
    funnel_counts = [df_raw[step].sum() for step in funnel_steps]
    total_entries = len(df_raw)
else:
    funnel_counts = [df_priority[step].sum() for step in funnel_steps]
    total_entries = len(df_priority)

# Calculate the percentage for each step
funnel_percentages = [(count / total_entries) * 100 for count in funnel_counts]

fig = go.Figure(go.Funnel(
    y = funnel_steps,
    x = funnel_percentages,
    textposition = "inside",
    textinfo = "value+percent initial",
    opacity = 0.65,
    marker = {
        "line": {"width": [4, 2, 2, 3, 1], "color": ["wheat", "wheat", "wheat", "wheat", "wheat"]}
    },
    connector = {"line": {"color": "royalblue", "dash": "dot", "width": 3}}
))

st.plotly_chart(fig)

selected_industry = st.sidebar.selectbox('Select the industry', sorted(df_raw['Industry'].unique()))
selected_role = st.sidebar.selectbox('Select the role', sorted(df_raw['Role'].unique()))

if selected_df == 'All data':
    df_filtered = df_raw[(df_raw['Industry'] == selected_industry) & (df_raw['Role'] == selected_role)]
else:
    df_filtered = df_priority[(df_priority['Industry'] == selected_industry) & (df_priority['Role'] == selected_role)]

funnel_counts_filtered = [df_filtered[step].sum() for step in funnel_steps]
total_entries_filtered = len(df_filtered)

funnel_percentages_filtered = [(count / total_entries_filtered) * 100 for count in funnel_counts_filtered]

st.title('Funnel Visualization with Filters')

fig_filtered = go.Figure(go.Funnel(
    y = funnel_steps,
    x = funnel_percentages_filtered,
    textposition = "inside",
    textinfo = "value+percent initial",
    opacity = 0.65,
    marker = {
        "line": {"width": [4, 2, 2, 3, 1], "color": ["wheat", "wheat", "wheat", "wheat", "wheat"]}
    },
    connector = {"line": {"color": "royalblue", "dash": "dot", "width": 3}}
))

st.plotly_chart(fig_filtered)