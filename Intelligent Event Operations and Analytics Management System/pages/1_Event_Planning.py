from animations import inject
inject()

import streamlit as st
from database import get_connection
from auth_guard import require_login
from floating_chatbot import floating_chatbot
floating_chatbot()
# ---------------- LOGIN PROTECTION ----------------
role = require_login()

st.title("Event Planning")

# ---------------- LOAD VENUES ----------------
conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT name FROM venues")
venues = [v[0] for v in cursor.fetchall()]

conn.close()

# ---------------- EVENT FORM ----------------
name = st.text_input("Event Name")

event_type = st.selectbox(
    "Type",
    ["Seminar", "Workshop", "Conference", "Hackathon", "Cultural Fest"]
)

date = st.date_input("Date")

venue = st.selectbox("Select Venue", venues)

planned_budget = st.number_input("Planned Budget", min_value=0.0)

# ---------------- CREATE EVENT ----------------
if st.button("Create Event"):

    if name == "":
        st.warning("Please enter event name")
        st.stop()

    if "username" not in st.session_state:
        st.error("Session expired. Please login again.")
        st.stop()

    conn = get_connection()
    cursor = conn.cursor()

    # ---------------- VENUE CONFLICT CHECK ----------------
    cursor.execute(
        """
        SELECT name, created_by
        FROM events
        WHERE venue=? AND date=?
        """,
        (venue, date)
    )

    conflict = cursor.fetchone()

    if conflict:

        existing_event = conflict[0]
        organizer = conflict[1]

        st.error(
            f"⚠ Venue already booked!\n\n"
            f"Event: {existing_event}\n"
            f"Organizer: {organizer}\n"
            f"Venue: {venue}\n"
            f"Date: {date}"
        )

        conn.close()
        st.stop()

    # ---------------- INSERT EVENT ----------------
    cursor.execute(
        """
        INSERT INTO events
        (name,type,date,venue,planned_budget,created_by)
        VALUES (?,?,?,?,?,?)
        """,
        (
            name,
            event_type,
            date,
            venue,
            planned_budget,
            st.session_state.username
        )
    )

    conn.commit()
    conn.close()

    st.success("✅ Event Created Successfully")

# ---------------- VIEW EVENTS ----------------

st.subheader("Existing Events")

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    """
    SELECT name, venue, date, created_by
    FROM events
    ORDER BY date DESC
    """
)

events = cursor.fetchall()
conn.close()

if events:

    for e in events:

        st.write(
            f"📅 {e[0]} | Venue: {e[1]} | Date: {e[2]} | Organizer: {e[3]}"
        )

else:

    st.info("No events created yet")