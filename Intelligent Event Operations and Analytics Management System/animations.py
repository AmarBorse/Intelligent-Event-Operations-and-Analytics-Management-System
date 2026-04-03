"""
animations.py
─────────────────────────────────────────────────────────────────────────────
Drop-in animation layer for the Intelligent Event Operations &
Analytics Management System.

ZERO changes to any existing .py file.

HOW IT WORKS
────────────
Streamlit renders HTML/CSS injected via st.markdown(unsafe_allow_html=True).
This file defines one function:  inject()
Import it at the top of any page (or app.py) like:

    from animations import inject
    inject()

That's it. All animations are pure CSS — no JS libraries, no side-effects.
─────────────────────────────────────────────────────────────────────────────
"""

import streamlit as st

def inject():
    st.markdown("""
<style>

/* ═══════════════════════════════════════════════════════════════════════════
   1.  KEYFRAME DEFINITIONS
═══════════════════════════════════════════════════════════════════════════ */

@keyframes fadeSlideDown {
    from { opacity: 0; transform: translateY(-22px); }
    to   { opacity: 1; transform: translateY(0);     }
}

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(22px); }
    to   { opacity: 1; transform: translateY(0);    }
}

@keyframes fadeSlideLeft {
    from { opacity: 0; transform: translateX(30px); }
    to   { opacity: 1; transform: translateX(0);    }
}

@keyframes fadeSlideRight {
    from { opacity: 0; transform: translateX(-30px); }
    to   { opacity: 1; transform: translateX(0);     }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}

@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.88); }
    to   { opacity: 1; transform: scale(1);    }
}

@keyframes shimmer {
    0%   { background-position: -500px 0; }
    100% { background-position:  500px 0; }
}

@keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0   rgba(13, 148, 136, 0.45); }
    50%       { box-shadow: 0 0 0 12px rgba(13, 148, 136, 0);   }
}

@keyframes borderGlow {
    0%, 100% { border-color: rgba(13,148,136,0.3); }
    50%       { border-color: rgba(13,148,136,0.9); }
}

@keyframes floatUpDown {
    0%, 100% { transform: translateY(0);    }
    50%       { transform: translateY(-6px); }
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

@keyframes countUp {
    from { opacity: 0; transform: scale(0.5); }
    to   { opacity: 1; transform: scale(1);   }
}

@keyframes progressFill {
    from { width: 0%; }
}

@keyframes ripple {
    to { transform: scale(4); opacity: 0; }
}

@keyframes slideInSidebar {
    from { opacity: 0; transform: translateX(-20px); }
    to   { opacity: 1; transform: translateX(0);     }
}

@keyframes gradientShift {
    0%   { background-position: 0%   50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0%   50%; }
}

@keyframes typewriter {
    from { clip-path: inset(0 100% 0 0); }
    to   { clip-path: inset(0 0%   0 0); }
}

@keyframes blink {
    50% { opacity: 0; }
}

/* ═══════════════════════════════════════════════════════════════════════════
   2.  PAGE & BODY  — animated gradient background
═══════════════════════════════════════════════════════════════════════════ */

.stApp {
    background: linear-gradient(
        135deg,
        #0F1E35 0%,
        #162540 25%,
        #1A2B4A 50%,
        #162540 75%,
        #0F1E35 100%
    );
    background-size: 400% 400%;
    animation: gradientShift 18s ease infinite;
}

/* ═══════════════════════════════════════════════════════════════════════════
   3.  PAGE TITLE  (h1)
═══════════════════════════════════════════════════════════════════════════ */

h1 {
    animation: fadeSlideDown 0.65s cubic-bezier(0.22,1,0.36,1) both;
    background: linear-gradient(90deg, #5EEAD4, #0D9488, #14B8A6, #F59E0B);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: fadeSlideDown 0.65s cubic-bezier(0.22,1,0.36,1) both,
               gradientShift 4s linear infinite;
}

/* ═══════════════════════════════════════════════════════════════════════════
   4.  SUBHEADINGS  (h2, h3)
═══════════════════════════════════════════════════════════════════════════ */

h2 {
    animation: fadeSlideRight 0.5s 0.1s cubic-bezier(0.22,1,0.36,1) both;
    position: relative;
    padding-left: 14px;
}

h2::before {
    content: '';
    position: absolute;
    left: 0; top: 10%; bottom: 10%;
    width: 4px;
    background: linear-gradient(180deg, #0D9488, #14B8A6);
    border-radius: 4px;
    animation: scaleIn 0.4s 0.25s ease both;
}

h3 {
    animation: fadeSlideRight 0.5s 0.15s cubic-bezier(0.22,1,0.36,1) both;
}

/* ═══════════════════════════════════════════════════════════════════════════
   5.  BUTTONS  — hover lift + glow + ripple
═══════════════════════════════════════════════════════════════════════════ */

.stButton > button {
    position: relative;
    overflow: hidden;
    transition: transform 0.22s ease,
                box-shadow 0.22s ease,
                background-color 0.22s ease,
                border-color 0.22s ease !important;
    animation: fadeSlideUp 0.4s 0.2s ease both;
    border-radius: 10px !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 8px 28px rgba(13,148,136,0.45) !important;
}

.stButton > button:active {
    transform: translateY(0) scale(0.97) !important;
    transition: transform 0.08s ease !important;
}

/* Primary button pulse ring */
.stButton > button[kind="primary"] {
    animation: fadeSlideUp 0.4s 0.2s ease both, pulse 2.5s 1.5s ease infinite;
}

/* ═══════════════════════════════════════════════════════════════════════════
   6.  INPUT FIELDS  — focus slide-in underline + glow
═══════════════════════════════════════════════════════════════════════════ */

.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input,
.stDateInput > div > div > input {
    transition: border-color 0.25s ease,
                box-shadow   0.25s ease,
                transform    0.20s ease !important;
    animation: fadeSlideUp 0.45s 0.1s ease both;
    border-radius: 8px !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus {
    box-shadow: 0 0 0 3px rgba(13,148,136,0.28),
                0 2px 12px rgba(13,148,136,0.18) !important;
    transform: translateY(-1px) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   7.  SELECT / DROPDOWN
═══════════════════════════════════════════════════════════════════════════ */

.stSelectbox > div > div {
    transition: box-shadow 0.25s ease, transform 0.2s ease !important;
    animation: fadeSlideUp 0.45s 0.12s ease both;
    border-radius: 8px !important;
}

.stSelectbox > div > div:hover {
    box-shadow: 0 0 0 2px rgba(13,148,136,0.4) !important;
    transform: translateY(-1px) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   8.  METRIC CARDS  — staggered fade + hover lift
═══════════════════════════════════════════════════════════════════════════ */

[data-testid="metric-container"] {
    animation: scaleIn 0.5s ease both;
    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
    border-radius: 14px !important;
    padding: 18px !important;
    background: rgba(26,43,74,0.7) !important;
    border: 1px solid rgba(13,148,136,0.18) !important;
    backdrop-filter: blur(8px) !important;
}

[data-testid="metric-container"]:hover {
    transform: translateY(-4px) scale(1.02) !important;
    box-shadow: 0 12px 32px rgba(13,148,136,0.25) !important;
    border-color: rgba(13,148,136,0.5) !important;
}

/* Stagger delays for multiple cards */
[data-testid="column"]:nth-child(1) [data-testid="metric-container"] {
    animation-delay: 0.05s;
}
[data-testid="column"]:nth-child(2) [data-testid="metric-container"] {
    animation-delay: 0.15s;
}
[data-testid="column"]:nth-child(3) [data-testid="metric-container"] {
    animation-delay: 0.25s;
}
[data-testid="column"]:nth-child(4) [data-testid="metric-container"] {
    animation-delay: 0.35s;
}

/* Metric value count-up feel */
[data-testid="stMetricValue"] {
    animation: countUp 0.6s cubic-bezier(0.34,1.56,0.64,1) both;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    color: #5EEAD4 !important;
}

[data-testid="stMetricLabel"] {
    animation: fadeIn 0.5s 0.3s ease both;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    color: #94A3B8 !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   9.  PROGRESS BAR  — animated fill
═══════════════════════════════════════════════════════════════════════════ */

.stProgress > div > div > div > div {
    animation: progressFill 1.2s cubic-bezier(0.4,0,0.2,1) both !important;
    background: linear-gradient(90deg, #0D9488, #14B8A6, #5EEAD4) !important;
    background-size: 200% auto !important;
    animation: progressFill 1.2s ease both,
               shimmer 2s linear infinite !important;
    border-radius: 10px !important;
}

.stProgress > div {
    border-radius: 10px !important;
    background: rgba(14,165,233,0.1) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   10. SIDEBAR  — animated nav items
═══════════════════════════════════════════════════════════════════════════ */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F1E35 0%, #1A2B4A 100%) !important;
    border-right: 1px solid rgba(13,148,136,0.2) !important;
    animation: fadeSlideLeft 0.5s ease both !important;
}

section[data-testid="stSidebar"] .stButton > button {
    animation: slideInSidebar 0.4s ease both;
    margin-bottom: 4px !important;
    width: 100% !important;
    text-align: left !important;
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    color: #CBD5E1 !important;
    font-weight: 500 !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(13,148,136,0.18) !important;
    border-color: rgba(13,148,136,0.4) !important;
    color: #5EEAD4 !important;
    transform: translateX(6px) !important;
    box-shadow: none !important;
}

/* Stagger sidebar items */
section[data-testid="stSidebar"] > div > div > div > div:nth-child(1) { animation-delay: 0.05s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(2) { animation-delay: 0.10s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(3) { animation-delay: 0.15s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(4) { animation-delay: 0.20s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(5) { animation-delay: 0.25s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(6) { animation-delay: 0.30s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(7) { animation-delay: 0.35s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(8) { animation-delay: 0.40s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(9) { animation-delay: 0.45s; }
section[data-testid="stSidebar"] > div > div > div > div:nth-child(10){ animation-delay: 0.50s; }

/* Sidebar header badge */
section[data-testid="stSidebar"] .stSuccess > div {
    background: rgba(13,148,136,0.18) !important;
    border: 1px solid rgba(13,148,136,0.4) !important;
    border-radius: 10px !important;
    animation: pulse 3s ease infinite !important;
    color: #5EEAD4 !important;
    font-weight: 600 !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   11. ALERTS — success / error / warning / info
═══════════════════════════════════════════════════════════════════════════ */

.stSuccess > div {
    animation: fadeSlideRight 0.4s ease both !important;
    border-left: 4px solid #10B981 !important;
    border-radius: 10px !important;
    background: rgba(16,185,129,0.1) !important;
}

.stError > div {
    animation: fadeSlideRight 0.4s ease both !important;
    border-left: 4px solid #EF4444 !important;
    border-radius: 10px !important;
    background: rgba(239,68,68,0.1) !important;
}

.stWarning > div {
    animation: fadeSlideRight 0.4s ease both !important;
    border-left: 4px solid #F59E0B !important;
    border-radius: 10px !important;
    background: rgba(245,158,11,0.1) !important;
}

.stInfo > div {
    animation: fadeSlideRight 0.4s ease both !important;
    border-left: 4px solid #3B82F6 !important;
    border-radius: 10px !important;
    background: rgba(59,130,246,0.1) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   12. DATAFRAMES / TABLES
═══════════════════════════════════════════════════════════════════════════ */

[data-testid="stDataFrame"] {
    animation: fadeSlideUp 0.5s 0.15s ease both;
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid rgba(13,148,136,0.18) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   13. EXPANDERS
═══════════════════════════════════════════════════════════════════════════ */

[data-testid="stExpander"] {
    animation: fadeSlideUp 0.4s ease both;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
}

[data-testid="stExpander"]:hover {
    border-color: rgba(13,148,136,0.4) !important;
    box-shadow: 0 4px 20px rgba(13,148,136,0.12) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   14. SLIDER  — animated thumb
═══════════════════════════════════════════════════════════════════════════ */

.stSlider > div > div > div > div {
    transition: transform 0.15s ease !important;
}

.stSlider > div > div > div > div:hover {
    transform: scale(1.3) !important;
}

[data-testid="stSlider"] {
    animation: fadeSlideUp 0.4s ease both;
}

/* ═══════════════════════════════════════════════════════════════════════════
   15. DIVIDERS
═══════════════════════════════════════════════════════════════════════════ */

hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg,
        transparent,
        rgba(13,148,136,0.6),
        rgba(94,234,212,0.4),
        rgba(13,148,136,0.6),
        transparent) !important;
    animation: fadeIn 0.6s ease both !important;
    margin: 20px 0 !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   16. SELECTBOX OPTIONS DROPDOWN
═══════════════════════════════════════════════════════════════════════════ */

[data-baseweb="popover"] {
    animation: scaleIn 0.2s ease both !important;
    transform-origin: top center !important;
    border-radius: 12px !important;
    border: 1px solid rgba(13,148,136,0.3) !important;
    box-shadow: 0 16px 40px rgba(0,0,0,0.4) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   17. CHECKBOX & RADIO  — animated check
═══════════════════════════════════════════════════════════════════════════ */

.stCheckbox > label > div:first-child,
.stRadio > div > label > div:first-child {
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    border-radius: 5px !important;
}

.stCheckbox > label > div:first-child:hover,
.stRadio > div > label > div:first-child:hover {
    transform: scale(1.15) !important;
    box-shadow: 0 0 0 3px rgba(13,148,136,0.3) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   18. COLUMN CONTAINERS  — staggered entry
═══════════════════════════════════════════════════════════════════════════ */

[data-testid="column"]:nth-child(1) { animation: fadeSlideUp 0.45s 0.00s ease both; }
[data-testid="column"]:nth-child(2) { animation: fadeSlideUp 0.45s 0.08s ease both; }
[data-testid="column"]:nth-child(3) { animation: fadeSlideUp 0.45s 0.16s ease both; }
[data-testid="column"]:nth-child(4) { animation: fadeSlideUp 0.45s 0.24s ease both; }

/* ═══════════════════════════════════════════════════════════════════════════
   19. PLOTLY CHARTS  — animated container entry
═══════════════════════════════════════════════════════════════════════════ */

[data-testid="stPlotlyChart"] {
    animation: scaleIn 0.55s 0.1s cubic-bezier(0.34,1.56,0.64,1) both;
    border-radius: 16px !important;
    border: 1px solid rgba(13,148,136,0.18) !important;
    padding: 8px !important;
    background: rgba(26,43,74,0.5) !important;
    transition: box-shadow 0.3s ease, transform 0.3s ease !important;
}

[data-testid="stPlotlyChart"]:hover {
    box-shadow: 0 12px 40px rgba(13,148,136,0.2) !important;
    transform: translateY(-2px) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   20. FLOATING CHATBOT  — bounce in + pulse
═══════════════════════════════════════════════════════════════════════════ */

/* Target the 💬 chat toggle button specifically */
.stButton > button[data-testid="baseButton-secondary"] {
    border-radius: 50% !important;
}

/* Chat box */
.chat-box {
    animation: scaleIn 0.3s cubic-bezier(0.34,1.56,0.64,1) both !important;
    transform-origin: bottom right !important;
    border: 1px solid rgba(13,148,136,0.35) !important;
    backdrop-filter: blur(12px) !important;
    background: rgba(15,30,53,0.95) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   21. LOADING SPINNER (Streamlit default)
═══════════════════════════════════════════════════════════════════════════ */

[data-testid="stSpinner"] > div {
    border-color: rgba(13,148,136,0.3) !important;
    border-top-color: #0D9488 !important;
    animation: spin 0.7s linear infinite !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   22. SCROLLBAR  — styled
═══════════════════════════════════════════════════════════════════════════ */

::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: rgba(26,43,74,0.5); border-radius: 3px; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #0D9488, #14B8A6);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover { background: #5EEAD4; }

/* ═══════════════════════════════════════════════════════════════════════════
   23. GLOBAL TEXT  — smooth rendering
═══════════════════════════════════════════════════════════════════════════ */

p, li, span, label {
    animation: fadeIn 0.4s ease both;
    line-height: 1.65 !important;
}

/* Write / st.write paragraph blocks */
[data-testid="stText"] {
    animation: fadeSlideUp 0.35s ease both;
}

/* ═══════════════════════════════════════════════════════════════════════════
   24. NUMBER INPUT  — animated arrows
═══════════════════════════════════════════════════════════════════════════ */

.stNumberInput button {
    transition: background 0.15s ease, transform 0.15s ease !important;
}

.stNumberInput button:hover {
    transform: scale(1.2) !important;
    background: rgba(13,148,136,0.3) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   25. DATE INPUT  — calendar
═══════════════════════════════════════════════════════════════════════════ */

.stDateInput > div {
    animation: fadeSlideUp 0.4s ease both;
    border-radius: 8px !important;
    transition: box-shadow 0.25s ease !important;
}

.stDateInput > div:focus-within {
    box-shadow: 0 0 0 3px rgba(13,148,136,0.28) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   26. FOOTER  — fade in at bottom
═══════════════════════════════════════════════════════════════════════════ */

footer {
    animation: fadeIn 1s 0.5s ease both;
}

footer:after {
    content: '🎯 Intelligent Event Operations & Analytics Management System';
    color: rgba(94,234,212,0.4) !important;
    font-size: 0.75rem !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   27. MAIN BLOCK  — overall page fade
═══════════════════════════════════════════════════════════════════════════ */

.main .block-container {
    animation: fadeSlideUp 0.5s cubic-bezier(0.22,1,0.36,1) both;
    padding-top: 2rem !important;
    max-width: 1100px !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   28. FORM SUBMIT BUTTON  — shimmer glow
═══════════════════════════════════════════════════════════════════════════ */

.stForm > div > div > div:last-child .stButton > button {
    background: linear-gradient(135deg, #0D9488, #14B8A6) !important;
    color: #fff !important;
    font-weight: 700 !important;
    padding: 12px 28px !important;
    border: none !important;
    overflow: hidden !important;
    position: relative !important;
}

.stForm > div > div > div:last-child .stButton > button::after {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
    animation: shimmer 2.5s 1s ease infinite;
}

/* ═══════════════════════════════════════════════════════════════════════════
   29. TAB NAVIGATION  — animated underline
═══════════════════════════════════════════════════════════════════════════ */

.stTabs [data-baseweb="tab-list"] {
    animation: fadeIn 0.5s ease both;
    border-bottom: 2px solid rgba(13,148,136,0.2) !important;
}

.stTabs [data-baseweb="tab"] {
    transition: color 0.2s ease, transform 0.2s ease !important;
    font-weight: 600 !important;
}

.stTabs [aria-selected="true"] {
    color: #5EEAD4 !important;
    transform: translateY(-1px) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   30. BALLOONS / SNOW  (native Streamlit)
═══════════════════════════════════════════════════════════════════════════ */

/* These use built-in keyframes, just style the container */
[data-testid="stDecoration"] {
    animation: fadeIn 0.5s ease both;
}

</style>
""", unsafe_allow_html=True)
