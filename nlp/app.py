import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "select an option",
    [
        "Classify it",
        "Question Answering",
        "Text generation",
        "Recognistion",
        "Summarize",
    ],
)

if option == "Classify it":
    text = st.text_area(label="Enter text")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
elif option == "Question Answering":
    q_a = pipeline("question-answering")
    context = st.text_area(label="Enter context")
    question = st.text_area(label=" Enter Question")
    if context and question:
        answer = q_a({"question": question, "context": context})
        st.write(answer)
elif option == "Text generation":
    text = st.text_area(label="Enter context")
    if text:
        text_generator = pipeline("text-generation")
        answer = text_generator(text)
        st.write(answer)
elif option == "Recognistion":
    text = st.text_area(label="Enter text")
    if text:
        text_recognition = pipeline("ner")
        answer = text_recognition(text)
        st.write(answer)
elif option == "Summarize":
    text = st.text_area(label="Enter text")
    if text:
        text_summarize = pipeline("summarization")
        answer = text_summarize(text, max_length=100, min_length=50)
        st.write(answer)
