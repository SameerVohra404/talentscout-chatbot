import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="TalentScout Hiring Assistant")

st.title("TalentScout Hiring Assistant")


# -------------------------
# SESSION STATE
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "state" not in st.session_state:
    st.session_state.state = {"step": 0}


# -------------------------
# RESET FUNCTION
# -------------------------

def reset_chat():
    st.session_state.messages = []
    st.session_state.state = {"step": 0}


# -------------------------
# SEND FUNCTION
# -------------------------

def send_message():

    text = st.session_state.user_input

    if text.strip() == "":
        return

    # save user message
    st.session_state.messages.append(
        {"role": "user", "content": text}
    )

    # bot response
    response = get_response(
        text,
        st.session_state.state
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.session_state.user_input = ""


# -------------------------
# AUTO START GREETING
# -------------------------

if len(st.session_state.messages) == 0:

    first_msg = get_response(
        "",
        st.session_state.state
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": first_msg}
    )


# -------------------------
# TOP BUTTONS
# -------------------------

col1, col2 = st.columns(2)

with col1:
    st.button("Restart Conversation", on_click=reset_chat)

with col2:
    st.write("Type 'exit' to stop")


# -------------------------
# CHAT DISPLAY
# -------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# -------------------------
# INPUT BOX
# -------------------------

st.text_input(
    "Type here",
    key="user_input",
    on_change=send_message
)