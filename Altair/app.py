import streamlit as st
import pandas as pd



from plotData import *


def main():
    page = st.sidebar.selectbox("Select Page", ["data", "Vaga lite", "Line Plot"])
    if page == "data":
        st.write(df.head(10))
    elif page == "Vaga lite":
        st.header("Vaga lite")
        vegalite()
    elif page == "Line Plot":
        st.header("Line Plot")
        LinePlot()


if __name__ == "__main__":
    main()
