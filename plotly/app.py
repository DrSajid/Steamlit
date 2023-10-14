import streamlit as st


import plotly.subplots as make_subplots


from plotData import *


plot = st.selectbox("Select a plot", ["Show data", "Pie Chart", "Donut Chart"])


def main():
    if plot == "Show data":
        ShowData()
    elif plot == "Pie Chart":
        pieChart()
    elif plot == "Donut Chart":
        Donut_Chart()


if __name__ == "__main__":
    main()
