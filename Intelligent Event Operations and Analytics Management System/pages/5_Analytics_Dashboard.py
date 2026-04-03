from animations import inject
inject()

import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_connection
from auth_guard import require_login

# ---------------- LOGIN ----------------
role = require_login()

st.title("Analytics Dashboard")

conn = get_connection()
cursor = conn.cursor()

# ---------------- GET EVENTS ----------------
cursor.execute("SELECT id,name,planned_budget FROM events")
events = cursor.fetchall()

data = []

for e in events:

    event_id = e[0]
    event_name = e[1]
    planned_budget = float(e[2])

    # ---------- ATTENDANCE ----------
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

    attendance_ratio = (attended/registered*100) if registered > 0 else 0

    # ---------- BUDGET ----------
    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE event_id=?",
        (event_id,)
    )

    actual_expense = cursor.fetchone()[0] or 0
    actual_expense = float(actual_expense)

    budget_eff = (actual_expense/planned_budget*100) if planned_budget > 0 else 0
    budget_eff = min(budget_eff,100)

    # ---------- FEEDBACK ----------
    cursor.execute(
        "SELECT AVG(rating) FROM feedback WHERE event_id=?",
        (event_id,)
    )

    feedback = cursor.fetchone()[0] or 0
    feedback_score = float(feedback) * 20

    # ---------- ESI ----------
    esi = (
        attendance_ratio * 0.3 +
        budget_eff * 0.3 +
        feedback_score * 0.4
    )

    # ---------- CATEGORY ----------
    if esi >= 80:
        category = "Excellent"
    elif esi >= 60:
        category = "Good"
    elif esi >= 40:
        category = "Average"
    else:
        category = "Poor"

    data.append([
        event_id,
        event_name,
        round(attendance_ratio,2),
        round(budget_eff,2),
        round(feedback_score,2),
        round(esi,2),
        category
    ])

# ---------------- DATAFRAME ----------------
df = pd.DataFrame(
    data,
    columns=[
        "Event ID",
        "Event",
        "Attendance %",
        "Budget %",
        "Feedback %",
        "ESI Score",
        "Category"
    ]
)

# ---------------- TABLE ----------------
st.subheader("Event Performance Table")

for index,row in df.iterrows():

    col1,col2,col3,col4,col5,col6,col7 = st.columns([2,1,1,1,1,1,1])

    col1.write(row["Event"])
    col2.write(row["Attendance %"])
    col3.write(row["Budget %"])
    col4.write(row["Feedback %"])
    col5.write(row["ESI Score"])
    col6.write(row["Category"])

    # ---------- DELETE BUTTON ----------
    if role == "Admin":
        if col7.button("Delete",key=row["Event ID"]):

            cursor.execute("DELETE FROM participants WHERE event_id=?",(row["Event ID"],))
            cursor.execute("DELETE FROM expenses WHERE event_id=?",(row["Event ID"],))
            cursor.execute("DELETE FROM feedback WHERE event_id=?",(row["Event ID"],))
            cursor.execute("DELETE FROM staff_assignments WHERE event_id=?",(row["Event ID"],))
            cursor.execute("DELETE FROM resource_allocations WHERE event_id=?",(row["Event ID"],))
            cursor.execute("DELETE FROM resource_requests WHERE event_id=?",(row["Event ID"],))
            cursor.execute("DELETE FROM staff_requests WHERE event_id=?",(row["Event ID"],))

            cursor.execute("DELETE FROM events WHERE id=?",(row["Event ID"],))

            conn.commit()

            st.success("Event Deleted Successfully")
            st.rerun()

# ---------------- CHART ----------------
st.subheader("Event Success Index Comparison")

fig = px.bar(
    df,
    x="Event",
    y="ESI Score",
    color="Category",
    text="ESI Score"
)

st.plotly_chart(fig,use_container_width=True)

# ---------------- INSIGHTS ----------------
st.subheader("Performance Insights")

if len(df) > 0:

    best_event = df.loc[df["ESI Score"].idxmax()]
    worst_event = df.loc[df["ESI Score"].idxmin()]
    avg_esi = df["ESI Score"].mean()

    st.success(
        f"🏆 Best Event: {best_event['Event']} ({best_event['ESI Score']})"
    )

    st.error(
        f"⚠ Worst Event: {worst_event['Event']} ({worst_event['ESI Score']})"
    )

    st.info(
        f"📊 Average ESI Across Events: {round(avg_esi,2)}"
    )

conn.close()