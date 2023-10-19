import streamlit as st
import pandas as pd


from plotData import *


def main():
    page = st.sidebar.selectbox(
        "Select Page",
        ["data", "Vaga lite", "Line Plot", "Bar chart", "Scatter plot", "Area Plot", "Scatter Matrics", "ScatterPlot_links", "HeatMap", "BarChart_H"],
    )
    if page == "data":
        st.write(df.head(10))
    elif page == "Vaga lite":
        st.header("Vaga lite")
        vegalite()
    elif page == "Line Plot":
        st.header("Line Plot")
        LinePlot()
    elif page == "Bar chart":
        st.header("Bar Chart")
        BarChart()
    elif page == "Scatter plot":
        st.header("Scatter plot")
        Scatter_plot()
    elif page == "Area Plot":
        st.header("Area Plot")
        Area_plot()
    elif page == "Scatter Matrics":
        st.header("Scatter Matrics")
        Scatter_Matrics()
    elif page == "ScatterPlot_links":
        st.header("ScatterPlot_links")
        ScatterPlot_links()
    elif page == "HeatMap":
        st.header("HeatMap")
        HeatMap()
    elif page == "BarChart_H":
        st.header("BarChart_H")
        BarChart_H()

if __name__ == "__main__":
    main()
