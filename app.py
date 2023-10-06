
import streamlit as st


from myplots import *


def main():
  page = st.sidebar.selectbox(
    "Select a Page",
    [
      "HomePage",
      "BarPlot",
      "Horizontal Bar plot",
      "Scatter Plot",
      "Histogram",
      "Pie Chart",
      "Two Subplots",
      "Four Subplots",
      "Four Axes"
    ]
  )
  if page == "HomePage":
    st.header("Data Application")
    """
    # Building apps with streamlit
    ## Please select a page on the left
    """
    st.balloons()
    st.write(df)
  elif page == "BarPlot":
    bar_chart()
  elif page == "Horizontal Bar plot":
    horizontal_bar()
  elif page == "Scatter Plot":
    visualize_scatter()
  elif page == "Histogram":
    st.header("Languages Histogram")
    histogram()
  elif page == "Pie Chart":
    st.header("Views and days pie chart")
    pie_chart()
  elif page == "Two Subplots":
    st.header("Two Subplots")
    two_subplots()
  elif page == "Four Subplots":
    st.header("Four Subplots")
    Four_subplots()
  elif page == "Four Axes":
    st.header("Four Axes")
    Four_Axes()






if __name__ == "__main__":
  main()