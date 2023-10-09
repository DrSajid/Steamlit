import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    df = pd.read_csv("../../data/donors/donor.csv")
    return df


df = load_data()
