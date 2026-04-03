Intelligent Event Operations & Analytics Management System

A full-stack web-based event management platform built using Python and Streamlit as an MCA Major Project at Pimpri Chinchwad University.


🔍 About the Project
This system goes beyond basic event management by integrating data analytics, NLP sentiment analysis, CSS animations, and intelligent performance scoring to help institutions manage and evaluate events effectively. The system uses SQLite as the database — no installation required, database is created automatically on first run. Pure CSS keyframe animations are applied across all pages via a dedicated animations.py module for a professional and responsive UI experience.

✨ Key Features

🔐 Role-Based Access — Admin and Organizer roles with SHA-256 encrypted login and session management
📅 Venue Conflict Detection — Automatically prevents double-booking of venues on same date
🎯 Event Success Index (ESI) — Custom weighted algorithm scoring every event out of 100
🧠 NLP Sentiment Analysis — TextBlob analyzes participant feedback as Positive / Neutral / Negative
💰 Budget Tracking — Real-time planned vs actual expense monitoring with overrun alerts
👥 Attendance Analytics — Register participants, mark attendance, track ratios and no-show %
📊 Analytics Dashboard — Plotly charts with best/worst event detection and ESI comparison
⚙️ Resource Management — Request and approval workflow with auto staff assignment
🤖 Rule-Based Chatbot — Floating assistant for event queries on every page (extendable to AI using OpenAI / Rasa)
🎨 CSS Animations — 18 keyframe animations including gradient background, slide-in pages, shimmer progress bars, and pulsing buttons


🛠️ Tech Stack
LayerTechnologyUI FrameworkStreamlit (multi-page web application)Frontend StructureHTML5 (via Streamlit)Frontend StylingCSS3 (injected via st.markdown)Frontend AnimationCSS Keyframe Animations (animations.py)BackendPython 3.10+DatabaseSQLite (auto-created as event_system.db)AnalyticsPandas, NumPyVisualizationPlotly ExpressNLPTextBlob / NLTKSecuritySHA-256 Encryption (Hashlib)Development EnvironmentPyCharm / Local Streamlit Server

📐 ESI Formula
ESI = (Attendance % × 0.3) + (Budget Efficiency % × 0.3) + (Feedback Score % × 0.4)

Feedback has the highest weight (0.4) because user satisfaction best defines event success.

ScoreCategory80 +✅ Excellent60 – 79🟦 Good40 – 59🟨 AverageBelow 40🔴 Poor

📁 Project Structure
Intelligent Event Operations & Analytics Management System/
├── app.py                          ← Login + Dashboard (entry point)
├── database.py                     ← SQLite connection + 10 table creation
├── auth_guard.py                   ← Page protection (require_login)
├── floating_chatbot.py             ← Sidebar chatbot (all pages)
├── animations.py                   ← 18 CSS keyframe animations (all pages)
├── .streamlit/
│   └── config.toml                 ← Theme config (dark navy + teal)
└── pages/
    ├── 0_Register.py               ← New organizer registration
    ├── 1_Event_Planning.py         ← Create events + conflict detection
    ├── 2_Budget_Management.py      ← Expenses + overrun alerts
    ├── 3_Participants.py           ← Attendance management
    ├── 4_Feedback.py               ← NLP sentiment analysis
    ├── 5_Analytics_Dashboard.py    ← ESI + Plotly charts
    ├── 6_Chatbot.py                ← Dedicated chatbot page
    ├── 7_Staff_Management.py       ← Staff and assignments
    ├── 8_Resource_Management.py    ← Resource requests + approval
    └── 9_User_Management.py        ← Admin only — manage organizers

🗄️ Database
Uses SQLite — no installation or server required. The database file event_system.db is automatically created on first run with all 10 tables:
users · events · venues · participants · expenses · feedback · staff · staff_assignments · resources · resource_requests

🚀 How to Run
1. Install dependencies
bashpip install streamlit pandas plotly textblob nltk
2. Run the project
bashstreamlit run app.py
3. Open in browser
http://localhost:8501
4. Default Admin login
Username: admin
Password: admin123

✅ No MySQL setup required. No database creation needed. Everything is automatic.


👤 User Roles
RoleAccessAdminFull access — all events, all users, approve resources, delete events, analyticsOrganizerOwn events only — create events, manage participants, budget, feedback, request resources

🎬 Animations Included
All animations are pure CSS — no JavaScript libraries needed.
ElementAnimationPage backgroundSlow animated gradient shiftPage title (h1)Slide down + animated gradient textButtonsLift on hover + glow shadow + pulse ringInput fieldsSlide up + glow on focusMetric cardsStaggered scale-in with hover liftProgress barsAnimated fill from 0% + shimmer sweepSidebar nav itemsStaggered slide-in with teal hoverAlertsSlide in from right with colored borderPlotly chartsBounce scale-in + hover liftDividersTeal gradient fade-in

📌 Important Notes

The chatbot is rule-based keyword matching — not AI. It can be extended using OpenAI API or Rasa NLP in future.
ESI feedback weight is 0.4 (highest) because user satisfaction is the most direct measure of event success.
Venue conflict detection runs a SQL query before every event save — same venue + same date is blocked automatically.
All passwords are encrypted using SHA-256 via Python's built-in hashlib library.


🚀 Future Scope

Upgrade chatbot to AI using OpenAI API / Rasa NLP
QR code-based automatic attendance marking
Predictive ESI using machine learning on historical data
Email / SMS alerts for budget overruns and approvals
PDF report export for administrators
Cloud deployment on AWS / Streamlit Cloud
Mobile app using React Native or Flutter


📚 References

Streamlit Documentation
TextBlob Documentation
Plotly Python Documentation
Pandas Documentation
Python SQLite3 Documentation
NLTK Documentation


👨‍💻 Author
Amar Borse
MCA — Pimpri Chinchwad University
Roll No: MCA24216
Guide: Prof. Pallavi Thorat
