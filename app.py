import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Tutor", layout="centered")

st.title("📘 AI Tutor with Automated Content Generator")

@st.cache_resource
def load_models():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    qa_pipeline = pipeline("question-answering")
    generator = pipeline("text-generation", model="gpt2")
    return summarizer, qa_pipeline, generator

summarizer, qa_pipeline, generator = load_models()

option = st.selectbox(
    "Choose Function",
    ["Generate Summary", "Question Answering", "Generate MCQs"]
)

if option == "Generate Summary":
    text = st.text_area("Enter Text")
    if st.button("Generate Summary"):
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        st.success(summary[0]['summary_text'])

elif option == "Question Answering":
    context = st.text_area("Enter Context")
    question = st.text_input("Enter Question")
    if st.button("Get Answer"):
        answer = qa_pipeline(question=question, context=context)
        st.success(answer['answer'])

elif option == "Generate MCQs":
    topic = st.text_input("Enter Topic")
    if st.button("Generate MCQs"):
        prompt = f"Generate 3 MCQs with options and answers on {topic}"
        mcqs = generator(prompt, max_length=200)
        st.success(mcqs[0]['generated_text'])
