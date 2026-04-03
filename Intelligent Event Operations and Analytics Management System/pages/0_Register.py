from animations import inject
inject()

import streamlit as st
from database import get_connection
import hashlib

st.title("User Registration")

def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()

username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Register"):

    if password != confirm:
        st.error("Passwords do not match")
    elif username == "":
        st.error("Username cannot be empty")
    else:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if user already exists
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            st.error("Username already exists")
        else:
            cursor.execute(
                "INSERT INTO users (username,password,role) VALUES (?,?,?)",
                (username, encrypt(password), "Organizer")
            )
            conn.commit()
            st.success("Registration Successful! You can now login.")

        conn.close()