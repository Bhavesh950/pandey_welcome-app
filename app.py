import streamlit as st
import time

# Page config
st.set_page_config(page_title="Pandey Special 💙", layout="centered")

# Custom CSS for styling + animations
st.markdown("""
    <style>
    body {
        background: radial-gradient(circle, #fef3c7, #fde68a);
        color: #4b0082;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #f59e0b;
        color: white;
        border-radius: 12px;
        font-size: 1.2rem;
        padding: 0.5rem 1.5rem;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #d97706;
    }
    .message {
        font-size: 1.5rem;
        border-right: 3px solid #f59e0b;
        white-space: nowrap;
        overflow: hidden;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .final-message {
        font-size: 1.3rem;
        text-align: center;
        font-weight: 600;
        color: #6b21a8;
        margin-top: 2rem;
    }
    .heart-float {
        position: fixed;
        bottom: 0;
        left: 50%;
        font-size: 2.5rem;
        color: #ef4444;
        animation: floatUp 5s ease-in infinite;
        user-select: none;
        pointer-events: none;
        opacity: 0.8;
        filter: drop-shadow(0 0 2px #f87171);
    }
    @keyframes floatUp {
        0% { transform: translateX(0) translateY(0) rotate(0deg); opacity: 0.8; }
        100% { transform: translateX(calc(-50vw + 50%)) translateY(-400px) rotate(360deg); opacity: 0; }
    }
    .firework {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 60px;
        animation: boom 1.2s ease-in-out infinite;
        opacity: 0.9;
        z-index: 9999;
    }
    @keyframes boom {
        0% { transform: scale(0.5) translate(-50%, -50%); opacity: 0.8; }
        50% { transform: scale(1.5) translate(-50%, -50%); opacity: 1; }
        100% { transform: scale(0.5) translate(-50%, -50%); opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

# Floating hearts
for i in range(5):
    st.markdown(f"""
        <div class="heart-float" style="left:{30 + i * 10}%; animation-delay: {i*1.5}s;">❤️</div>
    """, unsafe_allow_html=True)

# Session init
if 'msg_index' not in st.session_state:
    st.session_state.msg_index = 0
if 'show' not in st.session_state:
    st.session_state.show = False
if 'fireworks' not in st.session_state:
    st.session_state.fireworks = False
if 'music_playing' not in st.session_state:
    st.session_state.music_playing = False

# 🎆 Fireworks if triggered
if st.session_state.fireworks:
    st.markdown("""<div class="firework">🎆🎇✨</div>""", unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.fireworks = False

# 🧧 Title
st.title("Pandey Special 💙")

# 🔐 Unlock by Name
if not st.session_state.show:
    st.markdown("## 💌 Kya tu hi vo khaas insaan hai?")
    name = st.text_input("Apna naam likho (hint: jiska intezaar tha)", "")

    # 📦 Box animation
    st.markdown("<div style='font-size: 80px; text-align:center;'>📦</div>", unsafe_allow_html=True)

    # ✅ Right Name
    if name.lower().strip() == "pandey":
        st.success("Yes! Tum hi ho Pandey 💙")
        if st.button("🎁 Unlock Your Surprise"):
            st.session_state.show = True
            st.session_state.fireworks = True
            st.session_state.name = name
            st.rerun()
    elif name.strip() != "":
        st.error("🚫 Nahi bhai… ye gift Pandey ke liye hi hai!")
        st.button("🎁 Unlock Surprise", disabled=True)
    else:
        st.button("🎁 Unlock Surprise", disabled=True)
else:
    name = st.session_state.get("name", "Pandey")

    # 🎵 Music toggle
    if st.button("🎵 Play / Pause Music"):
        st.session_state.music_playing = not st.session_state.music_playing

    audio_url = "https://www.bensound.com/bensound-music/bensound-tomorrow.mp3"
    if st.session_state.music_playing:
        st.audio(audio_url, format="audio/mp3")

    # 💬 Messages
    messages = [
        f"{name}... ek mahine ka intezaar tha... ab tu saamne hai.",
        f"Tere bina hassi adhuri thi... vibe adhuri thi... din adhure the.",
        f"Teri yaadon se din guzarte the… par tu khud aayi, toh sab kuch wapas aagaya.",
        f"Tu meri dost hai... lekin usse bhi zyada meri sukoon wali feeling hai.",
        f"Missed You, {name}! 💙"
    ]

    # ⌨️ Typing effect
    def type_writer_effect(msg):
        typed = ""
        placeholder = st.empty()
        for char in msg:
            typed += char
            placeholder.markdown(f"<div class='message'>{typed}</div>", unsafe_allow_html=True)
            time.sleep(0.05)

    if st.session_state.msg_index < len(messages):
        type_writer_effect(messages[st.session_state.msg_index])
        time.sleep(2.5)
        st.session_state.msg_index += 1
        st.rerun()
    else:
        # 🖼️ Image slideshow
        slide_images = ["pandey_card.png", "pandey_heart.png", "pandey_star.png"]
        for img in slide_images:
            st.image(img, width=320)
            time.sleep(2)

        # ❤️ Final message
        st.markdown(f"""
            <div class='final-message'>
                Tu wapas aayi... toh lagta hai sab kuch wapas apna sa ho gaya.<br>
                Bas tu hamesha aise hi muskurati rehna, {name}. You're irreplaceable. 💙
            </div>
        """, unsafe_allow_html=True)
