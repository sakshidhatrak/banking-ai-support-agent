import sys
import os
import streamlit as st

# =========================================
# ADD PROJECT ROOT TO PATH
# =========================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# =========================================
# IMPORT BACKEND
# =========================================

from app.main import generate_response

# =========================================
# IMPORT FEEDBACK ENGINE
# =========================================

from feedback.feedback_manager import (
    process_feedback
)

from feedback.adaptation_engine import (
    get_adaptation_rules
)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Banking Support Agent",
    page_icon="🏦",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fb;
    }

    .title-style {
        font-size: 40px;
        font-weight: bold;
        color: #1f4e79;
    }

    .subtitle-style {
        font-size: 18px;
        color: #444444;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<p class="title-style">'
    '🏦 AI Banking Support Agent'
    '</p>',
    unsafe_allow_html=True
)


# =========================================
# INITIALIZE SESSION STATE
# =========================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

if "feedback_history" not in st.session_state:

    st.session_state.feedback_history = []

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    # -------------------------------------
    # CHAT HISTORY
    # -------------------------------------

    st.header("💬 Chat History")

    if st.session_state.chat_history:

        chat_counter = 1

        for role, message in reversed(
            st.session_state.chat_history
        ):

            if role == "user":

                short_message = message[:40]

                if len(message) > 40:

                    short_message += "..."

                st.markdown(
                    f"**{chat_counter}.** "
                    f"{short_message}"
                )

                chat_counter += 1

    else:

        st.info(
            "No conversations yet."
        )

    st.divider()

    # -------------------------------------
    # CURRENT ADAPTATION RULES
    # -------------------------------------

    st.subheader(
        "🧠 Current Adaptation Rules"
    )

    try:

        current_rules = (
            get_adaptation_rules()
        )

        st.json(current_rules)

    except Exception:

        st.warning(
            "Could not load adaptation rules."
        )

    st.divider()

    # -------------------------------------
    # CLEAR CHAT
    # -------------------------------------

    if st.button("🧹 Clear Chat"):

        # CLEAR CHAT HISTORY

        st.session_state.chat_history = []

        # CLEAR FEEDBACK HISTORY

        st.session_state.feedback_history = []

        # SUCCESS MESSAGE

        st.success(
            "Chat history cleared."
        )

        # FORCE UI REFRESH

        st.rerun()

# =========================================
# DISPLAY CHAT HISTORY
# =========================================

for role, message in (
    st.session_state.chat_history
):

    with st.chat_message(role):

        st.markdown(message)

# =========================================
# USER INPUT
# =========================================

user_query = st.chat_input(
    "Ask your banking-related question..."
)

# =========================================
# PROCESS USER QUERY
# =========================================

if user_query:

    # -------------------------------------
    # DISPLAY USER MESSAGE
    # -------------------------------------

    st.session_state.chat_history.append(
        ("user", user_query)
    )

    with st.chat_message("user"):

        st.markdown(user_query)

    # -------------------------------------
    # GENERATE RESPONSE
    # -------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Generating banking response..."
        ):

            try:

                response = generate_response(
                    user_query
                )

                st.markdown(response)

                st.session_state.chat_history.append(
                    ("assistant", response)
                )

            except Exception as error:

                st.error(
                    "Internal system error occurred."
                )

                st.exception(error)

# =========================================
# FEEDBACK SECTION
# =========================================

st.divider()

st.subheader("📝 Feedback")

feedback = st.text_input(
    "Provide optional feedback "
    "(too long / more detail / good response)"
)

if st.button("Submit Feedback"):

    if (
        feedback.strip()
        and st.session_state.chat_history
    ):

        latest_user_query = ""
        latest_response = ""

        for role, message in reversed(
            st.session_state.chat_history
        ):

            if (
                role == "assistant"
                and not latest_response
            ):

                latest_response = message

            elif (
                role == "user"
                and not latest_user_query
            ):

                latest_user_query = message

            if (
                latest_user_query
                and latest_response
            ):

                break

        # ---------------------------------
        # PROCESS FEEDBACK
        # ---------------------------------

        updated_rules = process_feedback(
            latest_user_query,
            latest_response,
            feedback
        )

        st.session_state.feedback_history.append(
            feedback
        )

        st.success(
            "Feedback saved successfully."
        )

        st.write(
            "Updated Behaviour Rules:"
        )

        st.json(updated_rules)

    else:

        st.warning(
            "No chat history available."
        )