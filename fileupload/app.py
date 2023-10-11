import pandas as pd
import streamlit as st
import time

progress = st.selectbox("Progress type", ["Progress bar", "Spinner"])

uploaded_file = st.file_uploader("Choose File", type=["csv"])


if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    if progress == "Progress bar":
        progress_bar = st.progress(0)
        for percentage_complete in range(100):
            progress_bar.progress(percentage_complete + 1)
            time.sleep(0.1)
    elif progress == "Spinner":
        with st.spinner("writing to DF..."):
            time.sleep(5)
            st.write(dataframe)
