import streamlit as st
from transformers import pipeline
from auth import login

st.set_page_config("AI Tutor")

if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    login()
    st.stop()

st.title("📘 AI Tutor – GenAI Based Learning System")

@st.cache_resource
def load_models():
    return (
        pipeline("summarization", model="facebook/bart-large-cnn"),
        pipeline("question-answering"),
        pipeline("text-generation", model="gpt2")
    )

summarizer, qa, generator = load_models()

option = st.selectbox("Choose Option",
                      ["Summary Generator", "Question Answering", "MCQ Generator"])

if option == "Summary Generator":
    text = st.text_area("Enter Text")
    if st.button("Generate"):
        st.success(summarizer(text, max_length=120)[0]['summary_text'])

elif option == "Question Answering":
    context = st.text_area("Context")
    question = st.text_input("Question")
    if st.button("Answer"):
        st.success(qa(question=question, context=context)['answer'])

elif option == "MCQ Generator":
    topic = st.text_input("Topic")
    if st.button("Generate MCQs"):
        st.success(generator(f"Generate MCQs on {topic}", max_length=200)[0]['generated_text'])
