import streamlit as st





from plotData import *


plot = st.selectbox(
    "Select a plot",
    ["Show data", "Pie Chart", "Donut Chart", "Scatter Plot", "Scatter with Columans", "Line Plot", "Bar plot", "Stack Barchar", "Animation", "Subplots"],
)


def main():
    if plot == "Show data":
        ShowData()
    elif plot == "Pie Chart":
        pieChart()
    elif plot == "Donut Chart":
        Donut_Chart()
    elif plot == "Scatter Plot":
        st.header("Scatter Plot")
        Scatter_Plot()
    elif plot == "Scatter with Columans":
        st.header("Scatter with Columans")
        Scatter_with_Columans()
    elif plot == "Line Plot":
        st.header("Line Plot")
        LinePlot()
    elif plot == "Bar plot":
        st.header("Bar plot")
        Bar_plot()
    elif plot == "Stack Barchar":
        st.header("Stack Barchar")
        Stack_Barchar()
    elif plot == "Animation":
        st.header("Animation")
        Animate()
    elif plot == "Subplots":
        st.header("Subplots")
        Subplots()

if __name__ == "__main__":
    main()
