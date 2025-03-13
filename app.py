import streamlit as st
import pandas as pd

# Set page title, icon, and layout
st.set_page_config(
    page_title="ASU Academic Calendar Chatbot",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for better readability and contrast
st.markdown(
    """
    <style>
        body {
            background-color: #181818; /* Darker background */
        }
        .title {
            color: #4B0082;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #ddd; /* Light grey for readability */
            margin-bottom: 30px;
        }
        .stTextInput > div > div > input {
            background-color: #252525 !important; /* Darker input field */
            color: #fff !important; /* White text */
            border: 2px solid #4B0082 !important;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stTextInput > div > div > input::placeholder {
            color: #aaa !important; /* Light grey placeholder */
        }
        .stButton>button {
            background-color: #4B0082;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
        }
        .event-card {
            background-color: #252525; /* Darker background for consistency */
            padding: 15px;
            border-radius: 10px;
            margin-top: 15px;
            box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.1);
            border-left: 5px solid #A855F7; /* Purple accent */
        }
        .event-title {
            color: #A855F7; /* Light purple title */
            font-size: 22px;
            font-weight: bold;
        }
        .event-text {
            color: #ffffff; /* White text for readability */
            font-size: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display Title and Subtitle
st.markdown("<h1 class='title'>🎓 ASU Academic Calendar Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Ask about important ASU academic dates, and I'll help you find them!</p>", unsafe_allow_html=True)

# ASU Calendar Data
data = {
    "Event": [
        "Classes Begin",
        "Last Day to Register",
        "Drop Deadline",
        "Tuition Fee Payment Deadline"
    ],
    "Session A": [
        "Jan 13, 2025",
        "Jan 14, 2025",
        "Jan 19, 2025",
        "Feb 25, 2025"
    ],
    "Session B": [
        "March 17, 2025",
        "March 18, 2025",
        "March 23, 2025",
        "Feb 25, 2025"
    ],
    "Session C": [
        "Jan 13, 2025",
        "Jan 18, 2025",
        "Jan 19, 2025",
        "Feb 25, 2025"
    ]
}

df = pd.DataFrame(data)

# User Query Input
user_input = st.text_input("🔍 Enter your query (e.g., When do classes begin?)")

# Process User Query
if user_input:
    user_input = user_input.lower()
    matched_event = None

    for event in df["Event"]:
        if event.lower() in user_input:
            matched_event = event
            break

    if matched_event:
        event_row = df[df["Event"] == matched_event]
        session_a = event_row["Session A"].values[0]
        session_b = event_row["Session B"].values[0]
        session_c = event_row["Session C"].values[0]

        # Display event results in a card with improved contrast
        st.markdown(
            f"""
            <div class='event-card'>
                <h3 class='event-title'>📅 {matched_event}</h3>
                <p class='event-text'><strong>Session A:</strong> {session_a}</p>
                <p class='event-text'><strong>Session B:</strong> {session_b}</p>
                <p class='event-text'><strong>Session C:</strong> {session_c}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("❌ Sorry, I couldn't find a matching date. Try rephrasing your query.")

# Show Full Calendar in an Elegant Table
with st.expander("📌 **View Full Academic Calendar**"):
    st.markdown("<div class='full-calendar'>", unsafe_allow_html=True)
    st.dataframe(df)
    st.markdown("</div>", unsafe_allow_html=True)

# Custom Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 14px;'>
        © 2025 ASU Academic Chatbot | Built using Streamlit
    </p>
    """,
    unsafe_allow_html=True
)