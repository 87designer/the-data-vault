import streamlit as st
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Projects", page_icon="📞", layout="wide")

Navbar()

# Projects Page
st.title("📂 Projects")
st.markdown("A showcase of my work.")
