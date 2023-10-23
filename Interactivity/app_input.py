import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_csv("../../data/ted.csv")

day = st.text_input("Day of the week", "Sunday")


if day is not None:
    dff = df[df["published_day"] == day]
    chart = (
        alt.Chart(dff)
        .mark_bar()
        .encode(
            x="published_year:O",
            y="sum(views)",
            color="sum(views)",
            tooltip=["sum(views)"],
        )
        .properties(width=650, height=500)
        .interactive()
    )
st.altair_chart(chart)
