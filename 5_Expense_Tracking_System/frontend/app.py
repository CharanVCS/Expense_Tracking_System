import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import category_analytics_tab, monthly_analytics_tab


st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics_by_Category", "Analytics_by_Monthly"])

with tab1:
    add_update_tab()

with tab2:
    category_analytics_tab()

with tab3:
    monthly_analytics_tab()

