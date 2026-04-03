import streamlit as st

def require_login():

    if "logged_in" not in st.session_state:
        st.error("⚠ Please login first")
        st.stop()

    if "role" not in st.session_state:
        st.error("⚠ Session error. Please login again.")
        st.stop()

    return st.session_state.role