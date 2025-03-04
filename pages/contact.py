import streamlit as st
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Contact", page_icon="📞", layout="wide")

Navbar()

# Page Content
st.title("📞 Contact Me")
st.markdown("Feel free to reach out!")
