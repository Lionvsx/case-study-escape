# pages/03_kpi_analysis.py
import streamlit as st
import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt
from streamlit_gsheets import GSheetsConnection


st.set_page_config(
    page_title="KPI | Escape Streamlit App",
    page_icon="📊",
)

st.title('KPIs and Hero KPI Analysis')

conn = st.connection("gsheets", type=GSheetsConnection)

df_priority = conn.read(
    worksheet=2085186136,
    ttl="30m",
)


def format_data(df):
    for col in ['Visited Website', 'Demo Booked', 'Demo Done', 'Meeting Planned', 'POC Started']:
        df[col] = df[col] == 'Yes'


format_data(df_priority)

demo_booked = df_priority['Demo Booked'].sum()
demo_done = df_priority['Demo Done'].sum()
visited_website = df_priority['Visited Website'].sum()
poc_started = df_priority['POC Started'].sum()
meeting_planned = df_priority['Meeting Planned'].sum()

conversion_rate_wesite_to_poc = poc_started / visited_website if visited_website else 0

st.metric("Visited Website to POC Conversion Rate", f"{conversion_rate_wesite_to_poc:.2%}")

conversion_rate = poc_started / demo_booked if demo_booked else 0

st.metric("Demo Booked to POC Conversion Rate", f"{conversion_rate:.2%}")

# Demo Done to POC
conversion_rate_demo_done_to_poc = poc_started / demo_done if demo_done else 0

st.metric("Demo Done to POC Conversion Rate", f"{conversion_rate_demo_done_to_poc:.2%}")

# Meeting Planned to POC
conversion_rate_meeting_planned_to_poc = poc_started / meeting_planned if meeting_planned else 0

st.metric("Meeting Planned to POC Conversion Rate", f"{conversion_rate_meeting_planned_to_poc:.2%}")

st.write("---")

# Calculate KPIs for each industry
industries = df_priority['Industry'].unique()
kpi_values = []

for industry in industries:
    df_filtered = df_priority[df_priority['Industry'] == industry]
    visited_website_filtered = df_filtered['Visited Website'].sum()
    poc_started_filtered = df_filtered['POC Started'].sum()
    conversion_rate_wesite_to_poc_filtered = poc_started_filtered / visited_website_filtered if visited_website_filtered else 0
    kpi_values.append(conversion_rate_wesite_to_poc_filtered)

df_kpis = pd.DataFrame({
    'Industry': industries,
    'KPI': kpi_values
})

# Create a bar plot
fig = px.bar(df_kpis, x='Industry', y='KPI', labels={'KPI': 'KPI (Visited Website to POC Conversion Rate)', 'Industry': 'Industry'}, title='KPIs by Industry')

# Display the plot
st.plotly_chart(fig)

st.write("---")

# Calculate KPIs for each role
roles = df_priority['Role'].unique()
kpi_values = []

for role in roles:
    df_filtered = df_priority[df_priority['Role'] == role]
    visited_website_filtered = df_filtered['Visited Website'].sum()
    poc_started_filtered = df_filtered['POC Started'].sum()
    conversion_rate_wesite_to_poc_filtered = poc_started_filtered / visited_website_filtered if visited_website_filtered else 0
    kpi_values.append(conversion_rate_wesite_to_poc_filtered)

df_role_kpis = pd.DataFrame({
    'Role': roles,
    'KPI': kpi_values
})

# Create a bar plot
fig = px.bar(df_role_kpis, x='Role', y='KPI', labels={'KPI': 'KPI (Visited Website to POC Conversion Rate)', 'Role': 'Role'}, title='KPIs by Role')

# Display the plot
st.plotly_chart(fig)




