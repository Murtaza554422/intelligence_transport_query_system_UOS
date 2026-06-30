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


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.image(
        "assets/developer.jpeg",
        width=180,
        
    )

    st.markdown("## 👨‍💻 Developer")

    st.markdown("""
    **Name:** Yasir Arafat

    **Degree:** BS Information Technology

    **University:** University Of Swat

    **Project:** Transport Intelligence & Query Resolution System
    """)

    st.divider()

    theme = st.radio(
        "🎨 Select Theme",
        ["Light", "Dark"]
    )

    st.session_state.theme = theme

    st.divider()

    st.markdown("## 📊 System Information")

    st.info("AI Model : Llama 3.3")

    st.info("Vector Database : FAISS")

    st.info("Knowledge Base : UOS BUSES INFO")

    st.divider()

    st.markdown("""
    ### 🚍 Features

    ✅ Bus Information

    ✅ Route Information

    ✅ Driver Details

    ✅ Fare Details

    ✅ Semester Charges

    ✅ AI Assistant
    """)


# ==================================================
# THEME COLORS
# ==================================================

if st.session_state.theme == "Dark":

    text_color = "#FFFFFF"

    # White glass card even in dark mode
    card_bg = "rgba(255,255,255,0.88)"

    card_text = "#000000"

else:

    text_color = "#000000"

    card_bg = "rgba(255,255,255,0.92)"

    card_text = "#000000"

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    f"""
<style>

.stApp {{
    
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    
}}

.main-card{{
    background-image: url("data:image/jpg;base64,{bg_image}");
    color:white;
    padding:25px;
    border-radius:20px;
    border:3px solid #2E7D32;
    box-shadow:0px 4px 20px rgba(0,0,0,0.25);
    backdrop-filter: blur(10px);
    font-weight:600;
}}

.header-title{{
    text-align:center;
    font-size:42px;
    font-weight:900;
    color:black;
    font-family: cooper black;
    text-shadow:
        2px 2px 6px rgba(0,0,0,0.8);
}}

.sub-title {{
    text-align:center;
    font-size:18px;
    color:black;
}}

.footer{{
    text-align:center;
    color:black;
    font-size: 20px;
    font-weight:bold;
    font-family: Bahnschrift SemiBold
    text-shadow:
        1px 1px 4px rgba(0,0,0,0.8);
}}
.stApp::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.30);
    z-index: -1;
}}
.sub-title{{
    text-align:center;
    font-size:20px;
    font-family: algerian;
    color:black;
    font-weight:700;
    text-shadow:
        1px 1px 4px rgba(0,0,0,0.8);
}}

.stChatInput{{
    background:white !important;
    color:black !important;
    border:2px solid black;
    border-radius:15px!important;
    font-weight:bold !important;
}}
[data-testid="stSidebar"]{{
    background:#FFDBBB;
    
}}
[data-testid="stSidebar"] *{{
    color:black !important;
    font-weight:600;
}}
</style>
""",
    unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================


# ---------------- CSS STYLING ----------------

st.markdown("""
<style>

/* Background (optional clean look) */
body {
    background-color: #0e1117;
}

/* Logo Animation */
.logo-animation {
    animation: floatLogo 3s ease-in-out infinite;
}

@keyframes floatLogo {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* Marquee Container */
.marquee {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    box-sizing: border-box;
    background: transparent;
}

/* Scrolling Text */
.marquee span {
    display: inline-block;
    padding-left: 100%;
    animation: scrollText 12s linear infinite;
    font-size: 36px;
    font-weight: bold;
    color: black;
    font-family: arial black;
    text-shadow: 1px 1px 1px red;
}

/* Animation */
@keyframes scrollText {
    0% {
        transform: translateX(0%);
    }
    100% {
        transform: translateX(-100%);
    }
}

/* Sub Title */
.sub-title {
    text-align: center;
    color: #00ff99;
    font-size: 18px;
    margin-top: -10px;
    font-weight: 700;
    text-shadow: 1px 1px 1px red;
}

/* Optional glow effect */
.glow-line {
    height: 2px;
    width: 100%;
    background: linear-gradient(to right, transparent, #00ff99, transparent);
    margin-top: 5px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1, 5])

# ---------------- LOGO ----------------
with col1:
    st.markdown('<div class="logo-animation">', unsafe_allow_html=True)
    st.image("assets/logo.jpg", width=120)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TITLE ----------------
with col2:
    st.markdown("""
    <div class="marquee">
        <span>
            UNIVERSITY OF SWAT — Transport Intelligence & Query Resolution System
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sub-title">
        AI-Powered Smart Transport & Query Management Platform
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ==================================================
# WELCOME CARD
# ==================================================

st.markdown("""
<div class='main-card'>

<h3>🚍 Welcome to University of Swat Transport Intelligence System</h3>

<p>
Ask questions about:
</p>

<ul>
<li>Bus Routes</li>
<li>Driver Information</li>
<li>Semester Fares</li>
<li>Daily Fares</li>
<li>Bus Capacity</li>
<li>Driver Contacts</li>
<li>Registration Numbers</li>
</ul>

</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# ==================================================
# LOAD CHATBOT
# ==================================================

if "chat" not in st.session_state:

    with st.spinner(
        "Loading Transport Knowledge Base..."
    ):

        st.session_state.chat = get_chain()


# ==================================================
# DISPLAY CHAT HISTORY
# ==================================================

for msg in st.session_state.chat.memory.chat_memory.messages:

    role = (
        "user"
        if msg.type == "human"
        else "assistant"
    )

    with st.chat_message(role):

        st.markdown(msg.content)


# ==================================================
# CHAT INPUT
# ==================================================

question = st.chat_input(
    "Ask about buses, routes, fares, drivers..."
)

if question:

    with st.chat_message("user"):

        st.markdown(question)

    with st.spinner("Thinking..."):

        result = st.session_state.chat(
            {"question": question}
        )

        answer = result["answer"]

    with st.chat_message("assistant"):

        st.markdown(answer)


# ==================================================
# FOOTER
# ==================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    f"""
<div class='footer'>

Final Year Project

Department Of Computer & Software technology (DCST)

University Of Swat

© 2026

</div>
""",
    unsafe_allow_html=True
)