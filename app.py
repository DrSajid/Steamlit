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
      "HomePage",
      "BarPlot",
      "Horizontal Bar plot"
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



def bar_chart():
  fig = plt.figure(figsize=(12,5))
  plt.xticks(rotation=70)
  bar_data = df.sort_values(by='views', ascending=False)
  bar_data = bar_data.head(20)
  plt.ticklabel_format(style="plain")
  plt.bar(bar_data['event'], bar_data['views'])
  plt.xlabel("Event")
  plt.ylabel("Views")
  plt.title("Events & View plot")
  st.pyplot(fig)


def horizontal_bar():
  fig = plt.figure(figsize=(12,5))
  plt.xticks(rotation=70)
  bar_data = df.sort_values(by='views', ascending=False)
  bar_data = bar_data.head(20)
  plt.ticklabel_format(style="plain")
  plt.barh(bar_data['event'], bar_data['views'])
  plt.ylabel("Event")
  plt.xlabel("Views")
  plt.title("Events & View plot")
  st.pyplot(fig)


if __name__ == "__main__":
  main()