from animations import inject
inject()

import streamlit as st
from database import get_connection
from auth_guard import require_login
from floating_chatbot import floating_chatbot
floating_chatbot()

# ---------------- LOGIN PROTECTION ----------------
role = require_login()

st.title("Budget Management")

# ---------------- LOAD EVENTS ----------------
conn = get_connection()
cursor = conn.cursor()

if role == "Admin":
    cursor.execute("SELECT id,name,planned_budget FROM events")
else:
    cursor.execute(
        "SELECT id,name,planned_budget FROM events WHERE created_by=?",
        (st.session_state.username,)
    )

events = cursor.fetchall()
conn.close()

if not events:
    st.warning("No events available.")
    st.stop()

# Convert events to dictionary
event_dict = {e[1]: (e[0], float(e[2])) for e in events}

selected_event = st.selectbox("Select Event", list(event_dict.keys()))

event_id, planned_budget = event_dict[selected_event]

# ---------------- ADD EXPENSE ----------------

st.subheader("Add Expense")

vendor = st.text_input("Vendor Name")

amount = st.number_input(
    "Expense Amount",
    min_value=0.0,
    step=100.0
)

if st.button("Add Expense"):

    if vendor == "":
        st.warning("Please enter vendor name")
        st.stop()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (event_id,vendor,amount) VALUES (?,?,?)",
        (event_id, vendor, amount)
    )

    conn.commit()
    conn.close()

    st.success("Expense Added Successfully")

# ---------------- CALCULATE EXPENSES ----------------

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    "SELECT SUM(amount) FROM expenses WHERE event_id=?",
    (event_id,)
)

actual_expense = cursor.fetchone()[0] or 0
actual_expense = float(actual_expense)

conn.close()

remaining_budget = planned_budget - actual_expense

budget_used_percent = (
    (actual_expense / planned_budget) * 100 if planned_budget > 0 else 0
)

# ---------------- BUDGET SUMMARY ----------------

st.subheader("Budget Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Planned Budget", f"₹{planned_budget:,.2f}")

with col2:
    st.metric("Total Expenses", f"₹{actual_expense:,.2f}")

with col3:
    st.metric("Remaining Budget", f"₹{remaining_budget:,.2f}")

# ---------------- PROGRESS BAR ----------------

st.progress(min(int(budget_used_percent), 100))

st.write(f"Budget Used: **{budget_used_percent:.2f}%**")

# ---------------- ALERT ----------------

if actual_expense > planned_budget:
    st.error("⚠ Budget Exceeded! You have spent more than the planned budget.")
else:
    st.success("Budget within limit.")