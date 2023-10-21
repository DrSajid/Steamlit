import streamlit as st
import pandas as pd


from plotData import *


def main():
    page = st.sidebar.selectbox(
        "Select Page",
        [
            "data",
            "Vaga lite",
            "Line Plot",
            "Bar chart",
            "Scatter plot",
            "Area Plot",
            "Scatter Matrics",
            "ScatterPlot_links",
            "HeatMap",
            "BarChart_H",
            "StackedBarChart",
            "StackedBarChart",
            "Normalized_StackedBarChart",
            "Normalized_SBarChart_text",
            "boxPlot",
            "Interactive Legend",
            "concatenated_legend",
            "dualY_axis",
            "concatenated_plot",
            "concatenated_plot_V",
            "Interactive_selection",
        ],
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
    elif page == "GroupBartChart":
        st.header("GroupBartChart")
        GroupBartChart()
    elif page == "StackedBarChart":
        st.header("StackedBarChart")
        StackedBarChart()
    elif page == "Normalized_StackedBarChart":
        st.header("Normalized_StackedBarChart")
        Normalized_StackedBarChart()
    elif page == "Normalized_SBarChart_text":
        st.header("Normalized_SBarChart_text")
        Normalized_SBarChart_text()
    elif page == "boxPlot":
        st.header("boxPlot")
        boxPlot()
    elif page == "Interactive Legend":
        st.header("Interactive Legend")
        Interactive_Legend()
    elif page == "concatenated_legend":
        st.header("concatenated_legend")
        concatenated_legend()
    elif page == "dualY_axis":
        st.header("dualY_axis")
        dualY_axis()
    elif page == "concatenated_plot":
        st.header("concatenated_plot")
        concatenated_plot()
    elif page == "concatenated_plot_V":
        st.header("concatenated_plot_V")
        concatenated_plot_V()
    elif page == "Interactive_selection":
        st.header("Interactive_selection")
        Interactive_selection()


if __name__ == "__main__":
    main()
