import streamlit as st
import pandas as pd
import altair as alt


def ohClicked():
    df = pd.read_csv("../../data/ted.csv")
    days = tuple(df["published_day"].unique())

    sdays = st.selectbox("Select Days", days)

    if sdays is not None:
        dff = df[df["published_day"] == sdays]
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


button = st.button("Please Click me", help="Click me to display", on_click=ohClicked)
