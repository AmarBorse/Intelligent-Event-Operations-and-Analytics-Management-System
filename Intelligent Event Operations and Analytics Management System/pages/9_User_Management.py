from animations import inject
inject()

import streamlit as st
from database import get_connection
import hashlib
from floating_chatbot import floating_chatbot
floating_chatbot()

st.title("User Management (Admin Only)")

if st.session_state.get("role") != "Admin":
    st.error("Access Denied")
    st.stop()


def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---------------- CREATE ORGANIZER ----------------

st.subheader("Create Organizer")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Create Organizer"):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        st.error("⚠ Username already exists")
    else:
        cursor.execute(
            "INSERT INTO users (username,password,role) VALUES (?,?,?)",
            (username, encrypt(password), "Organizer")
        )
        conn.commit()
        st.success("Organizer Created Successfully")

    conn.close()


# ---------------- SEARCH ORGANIZER ----------------

st.subheader("Search Organizer")

search_user = st.text_input("Enter organizer username")

if search_user:

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id,username FROM users WHERE role='Organizer' AND username LIKE ?",
        ("%" + search_user + "%",)
    )

    results = cursor.fetchall()

    conn.close()

    if results:
        for r in results:
            st.write(f"👤 {r[1]}")
    else:
        st.warning("No organizer found")


# ---------------- VIEW ORGANIZERS ----------------

st.subheader("All Organizers")

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT id,username FROM users WHERE role='Organizer'")
organizers = cursor.fetchall()

conn.close()

for org in organizers:

    col1, col2 = st.columns([4,1])

    with col1:
        st.write(f"👤 {org[1]}")

    with col2:
        if st.button("Delete", key=org[0]):

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM users WHERE id=?", (org[0],))
            conn.commit()
            conn.close()

            st.success("Organizer Deleted")
            st.rerun()


# ---------------- ORGANIZER ACTIVITY REPORT ----------------

st.subheader("Organizer Activity Report")

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT users.username, COUNT(events.id)
FROM users
LEFT JOIN events ON users.username = events.created_by
WHERE users.role='Organizer'
GROUP BY users.username
""")

report = cursor.fetchall()

conn.close()

for r in report:

    st.write(f"👤 {r[0]}  |  Events Created: {r[1]}")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM events WHERE created_by=?",
        (r[0],)
    )

    events = cursor.fetchall()
    conn.close()

    for e in events:
        st.write(f"   └ 📅 {e[0]}")