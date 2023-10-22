import streamlit as st
import pandas as pd
import datetime
import altair as alt


df = pd.read_csv("../../data/ted.csv")

start_date = st.date_input("Start Date if Publication", datetime.date(2006, 1, 1))

sd_pd = pd.to_datetime(start_date)

end_date = st.date_input(
    "End Date if Publication", datetime.date(sd_pd.year, sd_pd.month, sd_pd.day)
)


df["published_date"] = pd.to_datetime(df["published_date"])

if (start_date != None) & (end_date != None):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    dff = df[df["published_date"].isin(pd.date_range(start_date, end_date))]

    chart = (
        alt.Chart(dff)
        .mark_bar()
        .encode(
            x="published_year:O",
            y="sum(views)",
            color="published_day",
            tooltip=["sum(views)"],
        )
        .interactive()
        .properties(width=650, height=500)
    )

    st.altair_chart(chart)
