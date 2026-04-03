from animations import inject
inject()

import streamlit as st
import hashlib
from database import get_connection, init_db



init_db()

def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("Intelligent Event Management System")

if not st.session_state.logged_in:

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT role FROM users WHERE username=? AND password=?",
            (username, encrypt(password))
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            st.session_state.logged_in = True
            st.session_state.role = user[0]
            st.session_state.username = username
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Credentials")

else:
    st.sidebar.success(f"Logged in as {st.session_state.role}")

    if st.sidebar.button("Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.write("Use sidebar to navigate pages.")


    