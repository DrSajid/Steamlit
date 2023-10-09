import streamlit as st

from dataload import *
from myplots import *


def main():
    page = st.sidebar.selectbox(
        "Select a page on the left",
        ["data", "Count Plot", "Vilon & Strip Plot", "Bar Plot", "line Plot", "Figure and Axes"],
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
    elif page == "Figure and Axes":
        st.header("Figure and Axes")
        FigureAxes()

if __name__ == "__main__":
    main()
