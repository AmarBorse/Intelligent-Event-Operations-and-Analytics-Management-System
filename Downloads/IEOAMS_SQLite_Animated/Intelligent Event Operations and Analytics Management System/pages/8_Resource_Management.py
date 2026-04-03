from animations import inject
inject()

import streamlit as st
from database import get_connection
from auth_guard import require_login
from floating_chatbot import floating_chatbot
floating_chatbot()

role = require_login()

st.title("Resource Management")

conn = get_connection()
cursor = conn.cursor()

# ================= ADMIN PANEL =================
if role == "Admin":

    # ---------- ADD RESOURCE ----------
    st.subheader("➕ Add New Resource")

    col1, col2 = st.columns(2)

    with col1:
        resource_name = st.text_input("Resource Name")

    with col2:
        quantity = st.number_input("Total Quantity", min_value=1)

    staff_role = st.text_input("Staff Role Needed")

    if st.button("Add Resource"):

        cursor.execute(
            "INSERT INTO resources (name,quantity,staff_role) VALUES (?,?,?)",
            (resource_name, quantity, staff_role)
        )

        conn.commit()

        st.success("Resource Added Successfully")

    st.divider()

    # ---------- RESOURCE REQUESTS ----------
    st.subheader("📋 Resource Requests")

    cursor.execute("""
    SELECT resource_requests.id,
           events.name,
           requested_by,
           resource_name,
           quantity,
           status
    FROM resource_requests
    JOIN events ON events.id = resource_requests.event_id
    """)

    requests = cursor.fetchall()

    if not requests:
        st.info("No resource requests available")
    else:

        for r in requests:

            col1, col2, col3, col4, col5, col6 = st.columns([2,2,2,1,1,1])

            col1.write(r[1])  # Event
            col2.write(r[3])  # Resource
            col3.write(r[2])  # Requested by
            col4.write(r[4])  # Quantity
            col5.write(r[5])  # Status

            if r[5] == "Pending":
                if col6.button("Approve", key=r[0]):

                    cursor.execute(
                        "UPDATE resource_requests SET status='Approved' WHERE id=?",
                        (r[0],)
                    )

                    conn.commit()

                    st.success("Resource Request Approved")
                    st.rerun()

    st.divider()


# ================= ORGANIZER PANEL =================
else:

    st.subheader("📩 Request Resource")

    cursor.execute(
        "SELECT id,name FROM events WHERE created_by=?",
        (st.session_state.username,)
    )

    events = cursor.fetchall()

    if not events:
        st.warning("You have no events created.")
        st.stop()

    event_dict = {e[1]: e[0] for e in events}

    event_name = st.selectbox("Select Event", list(event_dict.keys()))

    resource_name = st.text_input("Resource Needed")

    qty = st.number_input("Quantity", min_value=1)

    if st.button("Send Request"):

        cursor.execute(
            """
            INSERT INTO resource_requests
            (event_id,requested_by,resource_name,quantity,status)
            VALUES (?,?,?,?,'Pending')
            """,
            (
                event_dict[event_name],
                st.session_state.username,
                resource_name,
                qty
            )
        )

        conn.commit()

        st.success("Resource Request Sent")

conn.close()