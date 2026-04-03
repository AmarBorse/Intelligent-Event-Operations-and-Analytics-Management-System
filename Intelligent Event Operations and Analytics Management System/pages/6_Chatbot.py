from animations import inject
inject()

import streamlit as st
from database import get_connection

st.title("🤖 AI Event Assistant")

query = st.text_input("Ask about upcoming events, history, contact...")

if query:
    conn = get_connection()
    cursor = conn.cursor()

    q = query.lower()

    if "upcoming" in q:
        cursor.execute("SELECT name,date FROM events WHERE date >= date('now')")
        events = cursor.fetchall()
        if events:
            for e in events:
                st.write(f"📅 {e[0]} on {e[1]}")
        else:
            st.write("No upcoming events.")

    elif "history" in q or "past" in q:
        cursor.execute("SELECT name,date FROM events WHERE date < date('now')")
        events = cursor.fetchall()
        if events:
            for e in events:
                st.write(f"🕒 {e[0]} on {e[1]}")
        else:
            st.write("No past events.")

    elif "contact" in q:
        st.write("📧 Organizer Contact: admin@gmail.com")

    elif "register" in q:
        st.write("👉 Use Register page from sidebar.")

    else:
        st.write("Try asking about upcoming events, past events, or contact.")

    conn.close()