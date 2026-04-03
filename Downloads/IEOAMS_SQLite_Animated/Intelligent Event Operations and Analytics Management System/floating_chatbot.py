import streamlit as st
from database import get_connection


def floating_chatbot():

    st.markdown("""
    <style>
    .chat-button {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #4CAF50;
        color: white;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 30px;
        text-align: center;
        line-height: 60px;
        cursor: pointer;
        z-index: 1000;
    }

    .chat-box {
        position: fixed;
        bottom: 100px;
        right: 30px;
        width: 300px;
        background: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #444;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False

    if st.button("💬", key="chat_toggle"):
        st.session_state.chat_open = not st.session_state.chat_open

    if st.session_state.chat_open:

        st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

        st.subheader("Event Assistant")

        query = st.text_input("Ask about upcoming events, history, contact")

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
                    st.write("No upcoming events")

            elif "history" in q:

                cursor.execute("SELECT name,date FROM events WHERE date < date('now')")
                events = cursor.fetchall()

                if events:
                    for e in events:
                        st.write(f"🕒 {e[0]} on {e[1]}")
                else:
                    st.write("No past events")

            elif "contact" in q:

                st.write("📧 Organizer Contact: admin@gmail.com")

            else:

                st.write("Try asking about upcoming events, past events, or contact")

            conn.close()

        st.markdown("</div>", unsafe_allow_html=True)