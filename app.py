import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
  df = pd.read_csv("../data/ted.csv")
  return df


df = load_data()


def main():
  page = st.sidebar.selectbox(
    "Select a Page",
    [
      "HomePage"
    ]
  )
  if page == "HomePage":
    st.header("Data Application")
    st.balloons()
    st.write(df)


if __name__ == "__main__":
  main()