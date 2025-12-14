import streamlit as st
from transformers import pipeline
from auth import auth_page

st.set_page_config("AI Tutor", page_icon="📘")

if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    auth_page()
    st.stop()

# ---------------- LOGOUT ----------------
st.sidebar.success(f"Welcome {st.session_state['user']}")
if st.sidebar.button("Logout"):
    st.session_state["login"] = False
    st.rerun()

# ---------------- AI TUTOR ----------------
st.title("📘 AI Tutor – GenAI Learning System")

@st.cache_resource
def load_models():
    return (
        pipeline("summarization", model="facebook/bart-large-cnn"),
        pipeline("question-answering"),
        pipeline("text-generation", model="gpt2")
    )

summarizer, qa, generator = load_models()

option = st.selectbox(
    "Choose Function",
    ["Generate Summary", "Question Answering", "Generate MCQs"]
)

if option == "Generate Summary":
    text = st.text_area("Enter Text")
    if st.button("Generate Summary"):
        st.success(summarizer(text, max_length=120)[0]['summary_text'])

elif option == "Question Answering":
    context = st.text_area("Enter Context")
    question = st.text_input("Enter Question")
    if st.button("Get Answer"):
        st.success(qa(question=question, context=context)['answer'])

elif option == "Generate MCQs":
    topic = st.text_input("Enter Topic")
    if st.button("Generate MCQs"):
        st.success(generator(f"Generate MCQs on {topic}", max_length=200)[0]['generated_text'])
