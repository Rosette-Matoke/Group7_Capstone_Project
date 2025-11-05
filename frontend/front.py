import streamlit as st
import requests

# ----------------- CONFIG -----------------
BACKEND_URL = "http://127.0.0.1:8000/predict"  # FastAPI endpoint

# ----------------- SESSION STATE -----------------
if "chat" not in st.session_state:
    st.session_state.chat = []  # Stores chat messages
if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # Input field

# ----------------- FUNCTIONS -----------------
def send_message():
    """
    Send the user's message to the backend and handle response
    """
    user_text = st.session_state.user_input.strip()
    if not user_text:
        return

    # Add user's message to chat
    st.session_state.chat.append(f"**You:** {user_text}")

    # Call backend API
    try:
        response = requests.post(BACKEND_URL, json={"text": user_text})
        data = response.json()
    except Exception as e:
        st.session_state.chat.append(f"**DoctorBot:** ⚠️ Error contacting backend: {e}")
        st.session_state.user_input = ""
        return

    # Parse bot response
    bot_msg = data.get("bot_message", "Sorry, something went wrong.")
    st.session_state.chat.append(f"**DoctorBot:** {bot_msg}")

    # Display follow-up questions if present
    follow_ups = data.get("follow_up", [])
    if follow_ups:
        st.session_state.chat.append(
            "**DoctorBot Follow-Up Questions:** " + ", ".join(follow_ups)
        )

    # Clear input safely
    st.session_state.user_input = ""

# ----------------- PAGE LAYOUT -----------------
st.set_page_config(page_title="DoctorBot", page_icon="🩺", layout="centered")

# Custom CSS for medical theme
st.markdown("""
<style>
body {background-color: #f0f8ff;}
.stTextInput>div>div>input {border-radius: 8px; padding: 10px;}
.stButton>button {background-color: #007ACC; color: white; border-radius: 8px; padding: 8px 15px;}
.stMarkdown {font-family: 'Arial', sans-serif;}
</style>
""", unsafe_allow_html=True)

st.title("🩺 DoctorBot")
st.markdown("Welcome! Enter your symptoms below, and I will give you possible conditions. Remember: This is **not a diagnosis**. Always consult a doctor.")

# ----------------- DISPLAY CHAT -----------------
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat:
        st.markdown(message)

# ----------------- USER INPUT -----------------
st.text_input("Your message:", key="user_input", on_change=send_message)

# ----------------- DISCLAIMER -----------------
st.markdown("---")
st.markdown("<small>⚠️ This chatbot provides informational guidance only. It does not replace professional medical advice, diagnosis, or treatment.</small>", unsafe_allow_html=True)
