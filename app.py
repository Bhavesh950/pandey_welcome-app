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
    /* Floating heart animation */
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
        0% {
            transform: translateX(0) translateY(0) rotate(0deg);
            opacity: 0.8;
        }
        100% {
            transform: translateX(calc(-50vw + 50%)) translateY(-400px) rotate(360deg);
            opacity: 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# Floating hearts (multiple)
for i in range(5):
    left_percent = 30 + i * 10
    st.markdown(f"""
        <div class="heart-float" style="left:{left_percent}%; animation-delay: {i*1.5}s;">❤️</div>
    """, unsafe_allow_html=True)

# Title
st.title("Pandey Special 💙")

# User input for name
name = st.text_input("Tera naam kya hai? (default: Pandey)", "Pandey")

# Music toggle button
if 'music_playing' not in st.session_state:
    st.session_state.music_playing = False

def toggle_music():
    st.session_state.music_playing = not st.session_state.music_playing

if st.button("🎵 Play / Pause Music"):
    toggle_music()

audio_url = "https://www.bensound.com/bensound-music/bensound-tomorrow.mp3"
if st.session_state.music_playing:
    st.audio(audio_url, format="audio/mp3")

# Messages (dynamic with name)
messages = [
    f"{name}... ek mahine ka intezaar tha... ab tu saamne hai.",
    f"Tere bina hassi adhuri thi... vibe adhuri thi... din adhure the.",
    f"Teri yaadon se din guzarte the… par tu khud aayi, toh sab kuch wapas aagaya.",
    f"Tu meri dost hai... lekin usse bhi zyada meri sukoon wali feeling hai.",
    f"Missed You, {name}! 💙"
]

# Session state init
if 'msg_index' not in st.session_state:
    st.session_state.msg_index = 0
if 'show' not in st.session_state:
    st.session_state.show = False

# Typing effect with fade-in like animation
def type_writer_effect(msg):
    typed = ""
    placeholder = st.empty()
    for char in msg:
        typed += char
        placeholder.markdown(f"<div class='message'>{typed}</div>", unsafe_allow_html=True)
        time.sleep(0.05)

# Images for slideshow after messages
slide_images = ["pandey_card.png", "pandey_heart.png", "pandey_star.png"]  # You can replace with your images

# Main Logic
if not st.session_state.show:
    if st.button("Tap to Begin…"):
        st.session_state.show = True
        st.rerun()
else:
    if st.session_state.msg_index < len(messages):
        type_writer_effect(messages[st.session_state.msg_index])
        time.sleep(2.5)
        st.session_state.msg_index += 1
        st.rerun()
    else:
        # Show slideshow of images with delay
        for img in slide_images:
            st.image(img, width=320)
            time.sleep(2)
        # Final emotional message
        st.markdown(f"""
            <div class='final-message'>
                Tu wapas aayi... toh lagta hai sab kuch wapas apna sa ho gaya.<br>
                Bas tu hamesha aise hi muskurati rehna, {name}. You're irreplaceable. 💙
            </div>
        """, unsafe_allow_html=True)
