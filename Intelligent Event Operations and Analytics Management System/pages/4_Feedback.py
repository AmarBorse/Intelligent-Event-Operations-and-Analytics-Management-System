from animations import inject
inject()

import streamlit as st
from database import get_connection
from textblob import TextBlob
from auth_guard import require_login
role = require_login()
from floating_chatbot import floating_chatbot
floating_chatbot()

st.title("Feedback & Sentiment Analysis")

conn = get_connection()
cursor = conn.cursor()

if st.session_state.role == "Admin":
    cursor.execute("SELECT id,name FROM events")
else:
    cursor.execute(
        "SELECT id,name FROM events WHERE created_by=?",
        (st.session_state.username,)
    )

events = cursor.fetchall()
conn.close()

if not events:
    st.warning("No events available.")
    st.stop()

event_dict = {e[1]: e[0] for e in events}
selected_event = st.selectbox("Select Event", list(event_dict.keys()))
event_id = event_dict[selected_event]

comment = st.text_area("Feedback Comment")
rating = st.slider("Rating",1,5)

if st.button("Submit Feedback"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO feedback (event_id,comment,rating) VALUES (?,?,?)",
        (event_id,comment,rating)
    )
    conn.commit()
    conn.close()
    st.success("Feedback Submitted")

if comment:
    polarity = TextBlob(comment).sentiment.polarity
    st.write("Sentiment Score:", polarity)