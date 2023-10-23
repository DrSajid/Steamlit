import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_csv("../../data/ted.csv")


days = tuple(df["published_day"].unique())

sdays = st.multiselect("Select Days", days)

if sdays is not None:
    dff = df[df["published_day"].isin(sdays)]
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
