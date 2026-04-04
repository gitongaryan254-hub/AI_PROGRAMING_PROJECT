import streamlit as st
import json
import os
from simple_chat_faq_bot_with_memory import normalize, get_response, load_memory, remember, print_welcome

# Page configuration
st.set_page_config(
    page_title="🤖 School Chat Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stTextInput > div > div > input {
        font-size: 16px;
    }
    .bot-message {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #ff4b4b;
    }
    .user-message {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #2196f3;
        text-align: right;
    }
    .welcome-text {
        text-align: center;
        color: #666;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for memory
if 'memory' not in st.session_state:
    st.session_state.memory = load_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar with information
with st.sidebar:
    st.title("🤖 Chat Bot Info")
    st.markdown("---")

    # Show welcome message in sidebar
    welcome_lines = [
        "🤖 school chat Bot (with JSON memory)",
        "",
        "Hello 😊 I'm your chat bot assistant for school registration details. I can help you learn about cybersecurity, education, Python and Git.",
        "",
        "Feel free to interact with me on any topic listed below—you can ask prompts as listed:",
        " - how do i register",
        " - what is cybersecurity",
        " - do i need coding",
        " - how to use python or git",
        " - how to push to github",
        "",
        "Type 'help' to see what I can do.",
        "Type 'history' to see a short summary of this session.",
        "Type 'exit' or 'quit' to leave the chat."
    ]

    for line in welcome_lines:
        st.text(line)

    st.markdown("---")
    st.markdown("### 📊 Session Stats")
    memory = load_memory()
    st.write(f"💬 Total conversations: {len(memory)}")

    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat history cleared!")

    if st.button("📚 Show Help"):
        st.info("I can help with: registration info, admission requirements, deadlines, fees, scholarships, study tips, cybersecurity basics, why cybersecurity matters, Python installation and basics, Git and GitHub commands, how to push code to GitHub, course structure, assessments, grading, and general school questions. Just ask in simple English!")

# Main chat interface
st.title("🤖 School Chat Bot")
st.markdown("*Your friendly assistant for school registration, cybersecurity, Python, and Git questions*")

# Chat container
chat_container = st.container()

# User input at the bottom
st.markdown("---")
user_input = st.text_input(
    "💬 Ask me anything:",
    placeholder="Type your question here... (e.g., 'how do I register?', 'what is cybersecurity?')",
    key="user_input"
)

# Process user input
if user_input and user_input.strip():
    # Get bot response
    bot_reply = get_response(user_input.strip())

    # Add to chat history
    st.session_state.chat_history.append({
        'user': user_input.strip(),
        'bot': bot_reply,
        'timestamp': st.session_state.get('timestamp', 0) + 1
    })

    # Save to memory
    remember(st.session_state.memory, user_input.strip(), bot_reply)

    # Clear input
    st.rerun()

# Display chat history
with chat_container:
    if st.session_state.chat_history:
        for i, chat in enumerate(st.session_state.chat_history):
            # User message
            st.markdown(f"""
            <div class="user-message">
                <strong>You:</strong> {chat['user']}
            </div>
            """, unsafe_allow_html=True)

            # Bot message
            st.markdown(f"""
            <div class="bot-message">
                <strong>🤖 Bot:</strong> {chat['bot']}
            </div>
            """, unsafe_allow_html=True)

            # Add some space between conversations
            if i < len(st.session_state.chat_history) - 1:
                st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="welcome-text">
            <h3>👋 Welcome to your Chat Bot!</h3>
            <p>I'm here to help you with school registration, cybersecurity questions, Python programming, and Git commands.</p>
            <p><strong>Try asking:</strong></p>
            <ul>
                <li>"how do I register for courses?"</li>
                <li>"what is cybersecurity?"</li>
                <li>"how to install Python?"</li>
                <li>"how to push to GitHub?"</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit • Memory saved to memory.json*")