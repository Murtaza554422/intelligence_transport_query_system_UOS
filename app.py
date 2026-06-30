import streamlit as st
import base64
from backend import get_chain


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="University Of Swat | Transport Intelligence System",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# HELPERS
# ==================================================

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "chat" not in st.session_state:
    st.session_state.chat = None


def get_ai():
    if st.session_state.chat is None:
        with st.spinner("Loading AI knowledge base..."):
            st.session_state.chat = get_chain()
    return st.session_state.chat


def ask_ai(query):
    chain = get_ai()
    result = chain({"question": query})
    return result["answer"]


# ==================================================
# GLOBAL CSS — MODERN / PROFESSIONAL THEME
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* App background */
.stApp {
    background: #ffffff;
    color: #111111;
}

/* Make default Streamlit text/headers dark on the white background */
[data-testid="stMarkdownContainer"], p, span, label, li {
    color: #111111;
}

/* ---------- MARQUEE (inside hero) ---------- */
.marquee-wrap {
    width: 100%;
    overflow: hidden;
    background: linear-gradient(135deg, #0ea5a3 0%, #14b8a6 35%, #2563eb 100%);
    border-radius: 10px;
    padding: 6px 0;
    margin-top: 14px;
}

.marquee-wrap span {
    display: inline-block;
    white-space: nowrap;
    padding-left: 100%;
    animation: scrollText 14s linear infinite;
    font-size: 18px;
    font-weight: 700;
    color:white;
    letter-spacing: 0.5px;
}

@keyframes scrollText {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-100%); }
}

@keyframes blink {
    0%, 49% { opacity: 1; }
    50%, 100% { opacity: 0.35; }
}

/* Hide default Streamlit chrome for a cleaner look */
#MainMenu, footer {visibility: hidden;}

/* Remove Streamlit's default black top toolbar */
header[data-testid="stHeader"] {
    background: #ffffff !important;
    box-shadow: none !important;
}

header[data-testid="stHeader"] * {
    color: #111111 !important;
}

div[data-testid="stDecoration"] {
    display: none !important;
}

div[data-testid="stToolbar"] {
    background: transparent !important;
}

/* Reduce default top spacing so header sits higher, but leave room so it isn't clipped */
.block-container {
    padding-top: 2.2rem !important;
}

.hero {
    margin-top: 0;
}
.hero {
    background: linear-gradient(135deg, #0ea5a3 0%, #14b8a6 35%, #2563eb 100%);
    border-radius: 18px;
    padding: 24px 32px;
    margin-bottom: 22px;
    box-shadow: 0 10px 30px rgba(13, 148, 136, 0.25);
    display: flex;
    flex-direction: column;
}

.hero-title {
    font-size: 28px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 0.3px;
    margin: 0;
}

.hero-subtitle {
    font-size: 14.5px;
    color: rgba(255,255,255,0.88);
    font-weight: 500;
    margin-top: 4px;
}



/* ---------- NAVBAR ---------- */
div[data-testid="column"] .stButton > button,
.stButton > button,
button[kind="secondary"],
button[data-testid="stBaseButton-secondary"] {
    width: 100% !important;
    background-color: #f3f4f6 !important;
    border: 1.5px solid #9ca3af !important;
    border-radius: 12px !important;
    padding: 10px 6px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    transition: all 0.25s ease !important;
}

div[data-testid="column"] .stButton > button,
div[data-testid="column"] .stButton > button *,
.stButton > button,
.stButton > button *,
button[kind="secondary"],
button[kind="secondary"] *,
button[data-testid="stBaseButton-secondary"],
button[data-testid="stBaseButton-secondary"] * {
    color: #111111 !important;
    font-weight: 600 !important;
    fill: #111111 !important;
}

div[data-testid="column"] .stButton > button:hover,
.stButton > button:hover,
button[kind="secondary"]:hover,
button[data-testid="stBaseButton-secondary"]:hover {
    background: linear-gradient(135deg, #14b8a6, #2563eb) !important;
    border-color: transparent !important;
    transform: translateY(-3px) scale(1.04);
    box-shadow: 0 8px 18px rgba(20, 184, 166, 0.4);
    cursor: pointer;
}

div[data-testid="column"] .stButton > button:hover,
div[data-testid="column"] .stButton > button:hover *,
.stButton > button:hover,
.stButton > button:hover *,
button[kind="secondary"]:hover,
button[kind="secondary"]:hover *,
button[data-testid="stBaseButton-secondary"]:hover,
button[data-testid="stBaseButton-secondary"]:hover * {
    color: #ffffff !important;
    fill: #ffffff !important;
}

div[data-testid="column"] .stButton > button:active {
    transform: translateY(-1px) scale(1.01);
}

/* ---------- CARDS ---------- */
.card {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 26px 28px;
    color: #111111;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.card h3 {
    margin-top: 0;
    color: #0d9488;
    font-weight: 700;
}

.card, .card p, .card li, .card span {
    color: #111111;
}

.section-title {
    font-size: 21px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 14px;
    border-left: 4px solid #14b8a6;
    padding-left: 12px;
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background: #f9fafb;
    border-right: 1px solid #e5e7eb;
}

section[data-testid="stSidebar"] * {
    color: #111111;
}

.dev-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 16px;
    text-align: center;
    margin-bottom: 14px;
}

.notice-box {
    background: #ecfdf5;
    border: 3px solid #99f6e4;
    border-radius: 12px;
    padding: 14px 16px;
    font-size: 13.5px;
    line-height: 1.9;
    color: #111111;
}

/* ---------- CHAT ---------- */
.stChatMessage {
    border-radius: 14px;
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    font-size: 12.5px;
    color: black;
    margin-top: 40px;
    padding-top: 18px;
    border-top: 1px solid #e5e7eb;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:
    st.markdown('<div class="dev-card">', unsafe_allow_html=True)
    st.image("assets/developer.jpeg", width=110)
    st.markdown("""
    **Yasir Arafat 
    BS Information Technology
    University of Swat** 
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("##### 📋 Transport Notice")
    st.markdown("""
    <div class="notice-box">
    🚌 Arrive 5 minutes before departure<br>
    🎓 Carry your transport card at all times<br>
    📞 Contact administration for route changes<br>
    ⚠️ Follow all university transport rules<br>
    🌟 Have a safe and comfortable journey
    </div>
    """, unsafe_allow_html=True)


# ==================================================
# HERO HEADER
# ==================================================

st.markdown("""
<div class="hero">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; width:100%;">
        <div>
            <p class="hero-title">🚌 University of Swat — Transport Intelligence System</p>
            <p class="hero-subtitle">AI-powered smart transport &amp; query management platform</p>
        </div>
        <div class="hero-badge"></div>
    </div>
    <div class="marquee-wrap">
        <span>🚌 UNIVERSITY OF SWAT — TRANSPORT INTELLIGENCE &amp; QUERY RESOLUTION SYSTEM 🚌</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ==================================================
# NAVIGATION
# ==================================================

pages = [
    ("🤖 AI Assistant", "AI"),
    ("🏠 Home", "Home"),
    ("🚍 Bus Info", "Bus"),
    ("🗺 Routes", "Routes"),
    ("👨‍✈ Drivers", "Drivers"),
    ("💰 Fares", "Fares"),
    ("🎓 Semester", "Semester"),
    
]

cols = st.columns(len(pages))
for i, (label, page) in enumerate(pages):
    with cols[i]:
        if st.button(label, key=page):
            st.session_state.page = page

st.write("")


# ==================================================
# PAGE ROUTING
# ==================================================

if st.session_state.page == "Home":
    st.markdown("""
    <div class="card">
        <h3>👋 Welcome</h3>
        <p>This system gives students and staff instant, AI-powered answers about
        university bus routes, schedules, drivers, and fares — available 24/7
        through the Assistant tab, or browse structured summaries using the
        navigation above.</p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "Bus":
    st.markdown('<p class="section-title">🚍 Bus Information</p>', unsafe_allow_html=True)
    with st.spinner("Analyzing bus data..."):
        answer = ask_ai("""
        Provide structured summary of all university buses:
        bus number, route, capacity, stops.
        """)
    st.markdown(f'<div class="card">{answer}</div>', unsafe_allow_html=True)

elif st.session_state.page == "Routes":
    st.markdown('<p class="section-title">🗺 Route Information</p>', unsafe_allow_html=True)
    with st.spinner("Loading routes..."):
        answer = ask_ai("Explain all transport routes with stops and destinations.")
    st.markdown(f'<div class="card">{answer}</div>', unsafe_allow_html=True)

elif st.session_state.page == "Drivers":
    st.markdown('<p class="section-title">👨‍✈ Driver Details</p>', unsafe_allow_html=True)
    with st.spinner("Fetching driver data..."):
        answer = ask_ai("List all drivers with names, contacts and assigned buses.")
    st.markdown(f'<div class="card">{answer}</div>', unsafe_allow_html=True)

elif st.session_state.page == "Fares":
    st.markdown('<p class="section-title">💰 Fare Details</p>', unsafe_allow_html=True)
    with st.spinner("Loading fares..."):
        answer = ask_ai("Explain transport fare system: daily and semester charges.")
    st.markdown(f'<div class="card">{answer}</div>', unsafe_allow_html=True)

elif st.session_state.page == "Semester":
    st.markdown('<p class="section-title">🎓 Semester Charges</p>', unsafe_allow_html=True)
    with st.spinner("Loading semester data..."):
        answer = ask_ai("Explain semester transport charges and policies.")
    st.markdown(f'<div class="card">{answer}</div>', unsafe_allow_html=True)

elif st.session_state.page == "AI":
    st.markdown('<p class="section-title">🤖 AI Assistant</p>', unsafe_allow_html=True)

    chain = get_ai()

    for msg in chain.memory.chat_memory.messages:
        role = "user" if msg.type == "human" else "assistant"
        with st.chat_message(role):
            st.markdown(msg.content)

    question = st.chat_input("Ask anything about the transport system...")

    if question:
        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Thinking..."):
            result = chain({"question": question})
            answer = result["answer"]

        with st.chat_message("assistant"):
            st.markdown(answer)


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">
    Final Year Project by Yasir Arafat · Department of Computer and Software Technology (DCST)
    · University of Swat · © 2026
</div>
""", unsafe_allow_html=True)