import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Welcome Pandey", layout="centered")

# Custom background and CSS animations
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #fde68a, #fef3c7, #ddd6fe);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .fade-in {
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .heart-float {
        position: absolute;
        animation: float 4s ease-in-out forwards;
        font-size: 24px;
    }
    @keyframes float {
        0% { bottom: 0; opacity: 0; }
        50% { opacity: 1; }
        100% { bottom: 100%; opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

# Title and welcome message
st.title("🎉 Welcome Pandey!")
st.markdown("<h4 style='text-align: center;'>This little surprise is made with ❤️, emotions, and beautiful memories...</h4>", unsafe_allow_html=True)

# Start button
if 'show' not in st.session_state:
    if st.button("💌 Unlock the Surprise"):
        st.session_state.show = True
        st.session_state.msg_index = 0
else:
    # Emotional message slides
    messages = [
        "Hey Pandey,",
        "This little web-app was created just for you...",
        "To welcome you back with care, respect, and pure emotions.",
        "It reflects friendship, creativity, and a sprinkle of magic 🌈.",
        "You've been missed, truly.",
        "Each moment is a memory — and you make them shine brighter ✨",
        "So here’s to your return, to our bond, and all the surprises ahead.",
        "Welcome back Pandey! ❤️"
    ]

    if st.session_state.msg_index < len(messages):
        with st.empty():
            for i in range(len(messages[st.session_state.msg_index])):
                st.markdown(f"<h2 style='text-align:center;'>{messages[st.session_state.msg_index][:i+1]}</h2>", unsafe_allow_html=True)
                time.sleep(0.06)
            time.sleep(1.5)
        st.session_state.msg_index += 1
        st.experimental_rerun()
    else:
        st.markdown("<h2 style='text-align:center; color: green;'>🎊 You're truly special, Pandey!</h2>", unsafe_allow_html=True)

        # Floating hearts button
        if st.button("Show some 💖"):
            for i in range(7):
                left = f"{20 + i*10}%"
                st.markdown(f"<div class='heart-float' style='left:{left}; animation-delay:{i*0.5}s;'>💖</div>", unsafe_allow_html=True)
            st.balloons()

        # Reset option
        if st.button("🔁 Replay Message"):
            for key in ["msg_index", "show"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# Special note at bottom
st.markdown("""
---
<h5 style='text-align:center;'>❤️ <i>Special Note:</i><br>
This surprise was made with care, respect, and pure emotions to celebrate the return of someone special.<br>
It reflects friendship, creativity, and a sprinkle of magic. 🌈</h5>
""", unsafe_allow_html=True)
