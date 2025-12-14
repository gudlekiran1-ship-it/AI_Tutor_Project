import streamlit as st
from db import get_db

def auth_page():
    st.title("🔐 AI Tutor Authentication")

    menu = ["Login", "Create Account"]
    choice = st.selectbox("Select Option", menu)

    if choice == "Login":
        login_user()
    else:
        register_user()

# ---------------- LOGIN ----------------
def login_user():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        result = cursor.fetchone()

        if result:
            st.session_state["login"] = True
            st.session_state["user"] = username
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Username or Password")

# ---------------- REGISTER ----------------
def register_user():
    st.subheader("Create New Account")

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")
    confirm_pass = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if new_pass != confirm_pass:
            st.error("Passwords do not match")
            return

        db = get_db()
        cursor = db.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (new_user, new_pass)
            )
            db.commit()
            st.success("Account Created Successfully 🎉")
            st.info("Go to Login Page")
        except:
            st.error("Username already exists")

