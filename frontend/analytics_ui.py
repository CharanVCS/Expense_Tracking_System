import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import altair as alt


API_URL = "http://localhost:8000"

def category_analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 1))

    
    if st.button('Get Analytics'):
        payload = {
            'startdate':start_date.strftime("%Y-%m-%d"),
            'enddate':end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics", json=payload)
        response = response.json()

        data = pd.DataFrame({
            "Category": list(response.keys()),
            "Total": [response[cate]['total'] for cate in response],
            "Percentage": [response[cate]['percentage'] for cate in response]
        })
        data_sorted = data.sort_values(by='Percentage', ascending=False)

        st.subheader('Expense BreakDown By Category')
        # st.bar_chart(data=data.set_index('Category')['Percentage'])
        
        chart = alt.Chart(data=data).mark_bar().encode(
            x=alt.X("Category" ,axis=alt.Axis(labelAngle=0)),
            y=alt.Y("Percentage")  # Labels are horizontal
        )
        text = alt.Chart(data).mark_text(dy=-10, size=12, color='white').encode(
            x="Category",
            y="Percentage",
            text="Percentage"
        )

        # Combine the bar chart and text labels
        final_chart = chart + text

        st.altair_chart(final_chart, use_container_width=True)

        st.table(data_sorted)

def monthly_analytics_tab():
    st.subheader('Monthly Expenses Analysis')

    if st.button('Get Monthly Analytics'):
        # payload = {
        #     'month': monthname
        # }

        response = requests.get(f"{API_URL}/monthly_analytics")
        data = response.json()
        df = pd.DataFrame(data)
        df.set_index('month_num', inplace=True)

        # st.bar_chart(data=df.set_index("month_name")['total_expenses'], width=0, height=0, use_container_width=True)
        
        chart = alt.Chart(data=df).mark_bar().encode(
            x=alt.X("month_name" ,axis=alt.Axis(labelAngle=0)),
            y=alt.Y("total_expenses")  # Labels are horizontal
        )
        text = alt.Chart(df).mark_text(dy=-10, size=12, color='white').encode(
            x="month_name",
            y="total_expenses",
            text="total_expenses"
        )

        # Combine the bar chart and text labels
        final_chart = chart + text

        st.altair_chart(final_chart, use_container_width=True)
        

        df["total_expenses"] = df["total_expenses"].map("{:.2f}".format)
        st.table(df.sort_index())


