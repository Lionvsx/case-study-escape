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

st.markdown("---")

st.markdown("""
### Funnel Visualization

**Objective:** To visualize the progression of leads through the sales funnel, identifying where the most significant drop-offs occur.

**Features:**

*   **Interactive Funnel Chart**: Display the number of leads at each funnel stage from initial contact to POC start.
*   **Filters for Industry and Role**: Allow users to refine the funnel view based on specific industries or roles, enabling targeted analysis of how different segments perform through the funnel.
*   **Comparison by Time Periods**: Optionally, include the ability to compare funnel performance across different time periods to track improvements or identify emerging challenges.

### Data Visualization with Filters

**Objective:** To enable detailed examination of leads post-demo booking, focusing on priorities assigned to each lead, which aids the sales team in prioritization.

**Features:**

*   **Filterable Data Table**: Present a comprehensive table of leads with columns for all relevant data, including the added 'Priority' column and a 'Demo Booked' indicator.
*   **Priority Filters**: Include filters to view leads based on their priority status, helping the sales team quickly identify high-priority leads.
*   **Demo Booked Filter**: A toggle to filter leads that have a demo booked (`True`/`False`), facilitating a focused view on leads at a critical decision-making stage.

### KPI Analysis

**Objective:** To provide a holistic and segmented analysis of key performance indicators that are crucial for evaluating the effectiveness and efficiency of the sales funnel.

**Features:**

*   **Global KPI Metrics**: Display overarching KPIs such as overall conversion rates, average lead response time, and demo completion rates that give insight into the funnel's health.
*   **Graphs per Industry and Role**: Offer detailed breakdowns of key metrics by industry and role, using bar charts or line graphs for visual comparison. This helps in understanding which segments are performing well and which require more attention.
""")

st.write("---")
st.write("Streamlit App by Leonard Roussard")