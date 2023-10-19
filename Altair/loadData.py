import pandas as pd
import streamlit as st
import altair as alt


@st.cache_data
def load_data():
    df = pd.read_csv("../../data/ted.csv")
    return df


df = load_data()
