import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_palette("deep")
sns.set_style("darkgrid")


@st.cache_data
def load_data():
    df = pd.read_csv("../../data/donors/donor.csv")
    return df


df = load_data()


def main():
    page = st.sidebar.selectbox("Select a page on the left", ["data", "Count Plot"])
    if page == "Count Plot":
        st.header("Count Plot")
        count_plot()
    if page == "data":
        st.header("Showing the data")
        st.write(df.head(10))


def count_plot():
    fig = plt.figure(figsize=(8, 6))
    plt.title("Prefix Countplot")
    plt.xticks(rotation=60, fontsize=12)
    sns.countplot(x="teacher_prefix", hue="project_is_approved", data=df)
    st.pyplot(fig)


if __name__ == "__main__":
    main()
