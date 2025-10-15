import streamlit as st
from datetime import datetime
from utils import get_answer_from_doc  # import the function from utils.py

# --- Streamlit Chatbot UI ---
st.set_page_config(page_title="📄 Docuchat Gemini Chatbot", layout="wide")
st.title("📄 Docuchat - Gemini Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("Upload your PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])

# --- Function to add message ---
def add_message(sender, text):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.chat_history.append({"sender": sender, "text": text, "time": timestamp})

# --- Function to send user input ---
def send_message():
    user_input = st.session_state.user_input
    if uploaded_file is None:
        st.warning("Please upload a document first!")
        return
    elif not user_input.strip():
        st.warning("Please enter a question!")
        return
    add_message("user", user_input)
    st.session_state.user_input = ""  # clear input
    with st.spinner("Generating answer..."):
        try:
            answer = get_answer_from_doc(uploaded_file, user_input)
            add_message("bot", answer)
        except Exception as e:
            add_message("bot", f"Error: {e}")

# --- Display chat history ---
chat_container = st.container()
for msg in st.session_state.chat_history:
    if msg["sender"] == "user":
        chat_container.markdown(
            f"""
            <div style='text-align:right; margin:5px 0; display:flex; justify-content:flex-end;'>
                <div style='background-color:#DCF8C6; color:#000; padding:10px; border-radius:15px; max-width:70%; word-wrap:break-word;'>
                    {msg['text']}<br>
                    <span style='font-size:10px; color:#555;'>{msg['time']}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        chat_container.markdown(
            f"""
            <div style='text-align:left; margin:5px 0; display:flex; justify-content:flex-start;'>
                <div style='background-color:#F1F0F0; color:#000; padding:10px; border-radius:15px; max-width:70%; word-wrap:break-word;'>
                    {msg['text']}<br>
                    <span style='font-size:10px; color:#555;'>{msg['time']}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
chat_container.markdown("<div style='clear:both'></div>", unsafe_allow_html=True)

# --- Input bar at bottom with Enter to send ---
with st.form(key="input_form", clear_on_submit=True):
    user_input = st.text_input("Type your question here:", key="user_input", placeholder="Type and press Enter to send...")
    submit_button = st.form_submit_button(label="Send", on_click=send_message)
