import streamlit as st
import time
import base64

# ---- Page Config ---- #
st.set_page_config(page_title="Welcome Back, Pandey!", layout="centered")

# ---- Custom CSS ---- #
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #fde68a, #fef3c7, #ddd6fe);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        border-radius: 12px;
        padding: 1rem;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .heart {
        color: red;
        font-size: 24px;
        animation: floatHearts 3s ease-in-out infinite;
    }

    @keyframes floatHearts {
        0% { transform: translateY(0); opacity: 1; }
        50% { transform: translateY(-10px); opacity: 0.8; }
        100% { transform: translateY(0); opacity: 1; }
    }

    .note {
        font-style: italic;
        color: #333;
        margin-top: 3rem;
        text-align: center;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Animation and Messages ---- #
def typewriter(message, delay=0.05):
    output = ""
    for char in message:
        output += char
        st.markdown(f"<h4 style='color:#444;'>{output}</h4>", unsafe_allow_html=True)
        time.sleep(delay)
        st.empty()
    st.markdown(f"<h4 style='color:#444;'>{output}</h4>", unsafe_allow_html=True)

def floating_hearts():
    st.markdown("""
        <div class="heart">❤️ ❤️ ❤️ ❤️ ❤️</div>
    """, unsafe_allow_html=True)

# ---- Main Content ---- #
if 'replay' not in st.session_state:
    st.session_state.replay = False

if st.button("▶️ Start the Surprise") or st.session_state.replay:
    st.session_state.replay = False
    messages = [
        "Hey Pandey... Welcome back! 🤗",
        "Things just weren’t the same without you.",
        "Your presence brings warmth, joy, and smiles.",
        "This little surprise is just for you...",
        "To remind you how much you're valued. ❤️",
        "Every line here holds a memory.",
        "Every word is filled with care.",
        "Ready to begin again — together. 😊"
    ]
    for msg in messages:
        typewriter(msg)
        time.sleep(1.2)

    floating_hearts()

    st.markdown("""
        <h2 style='text-align: center; margin-top: 2rem;'>💫 Welcome Back, Pandey! 💫</h2>
    """, unsafe_allow_html=True)

    if st.button("🔁 Replay Message"):
        st.session_state.replay = True
        st.experimental_rerun()

# ---- Special Note ---- #
st.markdown("""
<div class="note">
❤️ <strong>Special Note</strong><br>
This surprise was made with care, respect, and pure emotions to celebrate the return of someone special.<br>
It reflects friendship, creativity, and a sprinkle of magic. 🌈
</div>
""", unsafe_allow_html=True)

st.markdown("""
---
<center><sub>Made with ❤️ by Bhavesh for Pandey</sub></center>
""")
