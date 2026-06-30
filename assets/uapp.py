import streamlit as st
import base64
from backend import get_chain


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="University Of Swat Transport Intelligence System",
    page_icon="🚌",
    layout="wide"
)


# ==================================================
# BACKGROUND IMAGE
# ==================================================

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


bg_image = get_base64("assets/background.png")


# ==================================================
# SESSION STATE
# ==================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

if "page" not in st.session_state:
    st.session_state.page = "Home"


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.image("assets/developer.jpeg", width=180)

    st.markdown("## 👨‍💻 Developer")

    st.markdown("""
    **Name:** Yasir Arafat  
    **Degree:** BS Information Technology  
    **University:** University Of Swat  
    **Project:** Transport Intelligence & Query Resolution System
    """)

    st.divider()

    theme = st.radio("🎨 Select Theme", ["Light", "Dark"])
    st.session_state.theme = theme

    st.divider()

    st.markdown("## 📊 System Information")
    st.info("AI Model : Llama 3.3")
    st.info("Vector Database : FAISS")
    st.info("Knowledge Base : UOS BUSES INFO")

    st.divider()

    st.markdown("""
    ### 🚍 Features
    ✔ Bus Information  
    ✔ Route Information  
    ✔ Driver Details  
    ✔ Fare Details  
    ✔ Semester Charges  
    ✔ AI Assistant  
    """)


# ==================================================
# THEME COLORS
# ==================================================

if st.session_state.theme == "Dark":
    text_color = "#FFFFFF"
    card_bg = "rgba(255,255,255,0.88)"
    card_text = "#000000"
else:
    text_color = "#000000"
    card_bg = "rgba(255,255,255,0.92)"
    card_text = "#000000"


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(f"""
<style>

/* App background */
.stApp {{
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* overlay */
.stApp::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.30);
    z-index: -1;
}}

/* MAIN CARD */
.main-card{{
    background-image: url("data:image/jpg;base64,{bg_image}");
    padding:25px;
    border-radius:20px;
    border:3px solid #2E7D32;
    box-shadow:0px 4px 20px rgba(0,0,0,0.25);
    font-weight:600;
    color:white;
}}

/* LOGO ANIMATION */
.logo-animation {{
    animation: floatLogo 3s ease-in-out infinite;
}}

@keyframes floatLogo {{
    0% {{transform: translateY(0px);}}
    50% {{transform: translateY(-10px);}}
    100% {{transform: translateY(0px);}}
}}

/* ================= NAVBAR ================= */

.navbar {{
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
    margin: 15px 0;
}}

.nav-btn {{
    padding: 10px 18px;
    border-radius: 30px;
    font-weight: bold;
    font-size: 14px;
    cursor: pointer;
    border: 2px solid transparent;
    transition: 0.3s ease;
    background: rgba(255,255,255,0.85);
    color: black;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.2);
}}

.nav-btn:hover {{
    transform: scale(1.08);
    background: #00ff99;
    border: 2px solid black;
}}

.nav-active {{
    background: #00ff99 !important;
    color: black !important;
    border: 2px solid black !important;
}}

/* MARQUEE TITLE */
.marquee {{
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
}}

.marquee span {{
    display: inline-block;
    padding-left: 100%;
    animation: scrollText 12s linear infinite;
    font-size: 36px;
    font-weight: bold;
    color: black;
    font-family: arial black;
    text-shadow: 1px 1px 1px red;
}}

@keyframes scrollText {{
    0% {{transform: translateX(0%);}}
    100% {{transform: translateX(-100%);}}
}}

.sub-title {{
    text-align: center;
    font-size: 18px;
    font-weight: 700;
    color: black;
}}

.glow-line {{
    height: 2px;
    width: 100%;
    background: linear-gradient(to right, transparent, #00ff99, transparent);
    margin-top: 5px;
}}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

col1, col2 = st.columns([1, 5])

with col1:
    st.markdown('<div class="logo-animation">', unsafe_allow_html=True)
    st.image("assets/logo.jpg", width=120)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="marquee">
        <span>UNIVERSITY OF SWAT — Transport Intelligence & Query Resolution System</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sub-title">
        AI-Powered Smart Transport & Query Management Platform
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)


# ==================================================
# NAVIGATION BAR (CLICKABLE)
# ==================================================

st.markdown("---")

cols = st.columns(6)

pages = [
    ("🚍 Bus Info", "Bus"),
    ("🗺 Routes", "Routes"),
    ("👨‍✈ Drivers", "Drivers"),
    ("💰 Fares", "Fares"),
    ("🎓 Semester", "Semester"),
    ("🤖 AI Assistant", "AI")
]

for i, (label, page) in enumerate(pages):
    with cols[i]:
        if st.button(label, key=page):
            st.session_state.page = page

st.markdown("---")


# ==================================================
# PAGE CONTENT
# ==================================================

if st.session_state.page == "Home":
    st.markdown("""
    <div class='main-card'>
    <h3>🚍 Welcome to University of Swat Transport Intelligence System</h3>
    <p>Select a module from navigation bar above.</p>
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.page == "Bus":
    st.subheader("🚍 Bus Information")
    st.write("All bus details will be shown here.")

elif st.session_state.page == "Routes":
    st.subheader("🗺 Route Information")
    st.write("All route information here.")

elif st.session_state.page == "Drivers":
    st.subheader("👨‍✈ Driver Details")
    st.write("Driver details here.")

elif st.session_state.page == "Fares":
    st.subheader("💰 Fare Details")
    st.write("Fare structure here.")

elif st.session_state.page == "Semester":
    st.subheader("🎓 Semester Charges")
    st.write("Semester transport charges here.")

elif st.session_state.page == "AI":
    st.subheader("🤖 AI Assistant")


    # ==================================================
    # LOAD CHATBOT
    # ==================================================

    if "chat" not in st.session_state:
        with st.spinner("Loading Transport Knowledge Base..."):
            st.session_state.chat = get_chain()


    # Chat history
    for msg in st.session_state.chat.memory.chat_memory.messages:
        role = "user" if msg.type == "human" else "assistant"
        with st.chat_message(role):
            st.markdown(msg.content)


    # Input
    question = st.chat_input("Ask about buses, routes, fares, drivers...")

    if question:
        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Thinking..."):
            result = st.session_state.chat({"question": question})
            answer = result["answer"]

        with st.chat_message("assistant"):
            st.markdown(answer)


# ==================================================
# FOOTER
# ==================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
Final Year Project <br>
Department Of Computer & Software Technology (DCST) <br>
University Of Swat <br>
© 2026
</div>
""", unsafe_allow_html=True)