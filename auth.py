
import streamlit as st

def login():
    st.subheader("Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "admin":
            st.session_state["login"] = True
        else:
            st.error("Invalid Credentials")
