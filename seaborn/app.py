import streamlit as st

st.set_page_config(
    page_title="GeoScience Application",
    page_icon="",
    layout="centered",
    initial_sidebar_state="auto",
)

from dataload import *
from myplots import *
from PIL import Image

icon = Image.open("../../data/16627.jpg")


def main():
    st.image(icon, width=100)

    page = st.sidebar.selectbox(
        "Select a page on the left",
        [
            "data",
            "Count Plot",
            "Vilon & Strip Plot",
            "Bar Plot",
            "line Plot",
            "Sub plots",
            "Figure and Axes",
        ],
    )
    if page == "Count Plot":
        st.header("Count Plot")
        count_plot()
    elif page == "data":
        st.header("Showing the data")
        show_data()
    elif page == "Vilon & Strip Plot":
        st.header("Vilon & Strip Plot")
        violin_strip()
    elif page == "Bar Plot":
        st.header("Bar Plot")
        barplot()
    elif page == "line Plot":
        st.header("Line Plot")
        linePlot()
    elif page == "Sub plots":
        st.header("Subplots")
        Subplots()
    elif page == "Figure and Axes":
        st.header("Figure and Axes")
        FigureAxes()


if __name__ == "__main__":
    main()
