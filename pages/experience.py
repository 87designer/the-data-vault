import streamlit as st
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Experience", page_icon="📞", layout="wide")

Navbar()

# Experience Page
st.title("💼 Experience")
st.markdown("Here’s a timeline of my professional journey.")
