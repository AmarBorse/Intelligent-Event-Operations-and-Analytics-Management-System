from animations import inject
inject()

import streamlit as st
from database import get_connection
from auth_guard import require_login
from floating_chatbot import floating_chatbot
floating_chatbot()

role = require_login()

st.title("Staff & Volunteer Management")

conn = get_connection()
cursor = conn.cursor()

# ================= ADMIN PANEL =================
if role == "Admin":

    # -------- ADD STAFF --------
    st.subheader("➕ Add Staff Member")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Staff Name")

    with col2:
        role_name = st.text_input("Role (Technician / Volunteer / Security)")

    phone = st.text_input("Phone Number")

    if st.button("Add Staff"):

        if name == "" or role_name == "":
            st.warning("Please enter required details")
        else:
            cursor.execute(
                "INSERT INTO staff (name,role,phone) VALUES (?,?,?)",
                (name, role_name, phone)
            )

            conn.commit()

            st.success("Staff Added Successfully")

    st.divider()

    # -------- VIEW STAFF --------
    st.subheader("👥 Available Staff")

    cursor.execute("SELECT id,name,role,phone FROM staff")

    staff = cursor.fetchall()

    if not staff:
        st.info("No staff added yet")
    else:

        for s in staff:

            col1, col2, col3, col4 = st.columns([2,2,2,1])

            col1.write(s[1])
            col2.write(s[2])
            col3.write(s[3])

            if col4.button("Remove", key=s[0]):

                cursor.execute(
                    "DELETE FROM staff WHERE id=?",
                    (s[0],)
                )

                conn.commit()

                st.success("Staff Removed")
                st.rerun()

    st.divider()

    # -------- STAFF ASSIGNMENTS --------
    st.subheader("📌 Staff Assignments")

    cursor.execute("""
    SELECT events.name,
           staff.name,
           staff_assignments.duty
    FROM staff_assignments
    JOIN events ON events.id = staff_assignments.event_id
    JOIN staff ON staff.id = staff_assignments.staff_id
    """)

    assignments = cursor.fetchall()

    if assignments:

        for a in assignments:

            st.write(
                f"Event: **{a[0]}**  |  Staff: **{a[1]}**  |  Duty: **{a[2]}**"
            )

    else:

        st.info("No staff assigned yet")

# ================= ORGANIZER PANEL =================
else:

    st.subheader("Staff Information")

    st.info(
        "Staff will be automatically assigned when Admin approves resource requests."
    )

conn.close()