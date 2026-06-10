import streamlit as st

st.set_page_config(
    page_title="Matchbook Log Analyser",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

dashboard_page = st.Page("pages/dashboard.py")

pg = st.navigation([dashboard_page])
pg.run()
