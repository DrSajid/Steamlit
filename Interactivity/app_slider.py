import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_csv("../../data/ted.csv")


df["published_date"] = pd.to_datetime(df["published_date"])

years = df["published_year"].unique()



min_year = years.min()
max_year = years.max()


syear, eyear = st.select_slider(
    "Select year range", options=list(years), value=(min_year, max_year)
)


if (syear is not None) & (eyear is not None):
    syear = pd.to_datetime(syear, format="%Y")
    eyear = pd.to_datetime(eyear, format="%Y")
    dff = df[df["published_date"].isin(pd.date_range(syear, eyear))]

    chart = (
        alt.Chart(dff)
        .mark_bar()
        .encode(
            x="published_year:O",
            y="sum(views)",
            color="published_day",
        )
        .properties(width=650, height=500)
        .interactive()
    )
    st.altair_chart(chart)
