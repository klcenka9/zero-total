import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="ZeroTotal - File Scanner",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit branding
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp { margin: 0; padding: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_content = Path("index.html").read_text(encoding="utf-8")

st.components.v1.html(html_content, height=1200, scrolling=True)
