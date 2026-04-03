from animations import inject
inject()

import streamlit as st
from database import get_connection
from auth_guard import require_login

# ---------------- LOGIN PROTECTION ----------------
role = require_login()

st.title("Participants & Attendance")

conn = get_connection()
cursor = conn.cursor()

# =====================================================
# LOAD EVENTS
# =====================================================

if role == "Admin":
    cursor.execute("SELECT id,name FROM events")
else:
    cursor.execute(
        "SELECT id,name FROM events WHERE created_by=?",
        (st.session_state.username,)
    )

events = cursor.fetchall()

if not events:
    st.warning("No events available.")
    st.stop()

event_dict = {e[1]: e[0] for e in events}

selected_event = st.selectbox("Select Event", list(event_dict.keys()))
event_id = event_dict[selected_event]

st.divider()

# =====================================================
# REGISTER PARTICIPANT
# =====================================================

st.subheader("➕ Register Participant")

name = st.text_input("Participant Name")

if st.button("Register Participant"):

    if name == "":
        st.warning("Enter participant name")
    else:

        cursor.execute(
            """
            INSERT INTO participants (event_id,name,attended)
            VALUES (?,?,0)
            """,
            (event_id, name)
        )

        conn.commit()

        st.success("Participant Registered")
        st.rerun()

st.divider()

# =====================================================
# PARTICIPANT ACTIONS
# =====================================================

st.subheader("📋 Manage Participants")

cursor.execute(
    """
    SELECT id,name FROM participants
    WHERE event_id=?
    """,
    (event_id,)
)

participants = cursor.fetchall()

if participants:

    participant_dict = {p[1]: p[0] for p in participants}

    selected_participant = st.selectbox(
        "Select Participant",
        list(participant_dict.keys())
    )

    col1, col2, col3 = st.columns(3)

    # ---------------- MARK ATTENDANCE ----------------
    with col1:
        if st.button("Mark Attended"):

            cursor.execute(
                """
                UPDATE participants
                SET attended=1
                WHERE id=?
                """,
                (participant_dict[selected_participant],)
            )

            conn.commit()

            st.success("Attendance Marked")
            st.rerun()

    # ---------------- REMOVE ATTENDANCE ----------------
    with col2:
        if st.button("Remove Attendance"):

            cursor.execute(
                """
                UPDATE participants
                SET attended=0
                WHERE id=?
                """,
                (participant_dict[selected_participant],)
            )

            conn.commit()

            st.success("Attendance Removed")
            st.rerun()

    # ---------------- DELETE PARTICIPANT ----------------
    with col3:
        if st.button("Delete Participant"):

            cursor.execute(
                """
                DELETE FROM participants
                WHERE id=?
                """,
                (participant_dict[selected_participant],)
            )

            conn.commit()

            st.success("Participant Deleted")
            st.rerun()

else:
    st.info("No participants registered yet")

st.divider()

# =====================================================
# ATTENDANCE ANALYTICS
# =====================================================

cursor.execute(
    "SELECT COUNT(*) FROM participants WHERE event_id=?",
    (event_id,)
)

registered = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM participants WHERE event_id=? AND attended=1",
    (event_id,)
)

attended = cursor.fetchone()[0]

attendance_ratio = (attended / registered * 100) if registered > 0 else 0
no_show = 100 - attendance_ratio

st.subheader("📊 Attendance Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Registered", registered)
col2.metric("Attended", attended)
col3.metric("Attendance %", f"{attendance_ratio:.1f}%")
col4.metric("No Show %", f"{no_show:.1f}%")

st.progress(int(attendance_ratio))

conn.close()