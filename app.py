import streamlit as st
import os
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Home", page_icon="💻", layout="wide")

Navbar()

# Logo
# HORIZONTAL_BLUE = "assets/images/RR_Logo.svg"
# HORIZONTAL_WHITE = "assets/images/RR_Logo_dm.svg"

# st.logo(HORIZONTAL_BLUE, icon_image=HORIZONTAL_WHITE)


# Home Page
st.title("Welcome to My Data Vault 👋")
st.write("\n")

col1, col2 = st.columns([2, 1])
col1.markdown("""A Dynamic, Interactive Tech Portfolio, that is a self-hosted, AI-powered online resume showcasing my skills, experience, and projects with interactive data visualizations, API integrations, and AI-driven insights.""")
col1.write("\n")
col1.markdown("""
- 🚀 **Data Science Developer** with experience in Python, FastAPI, and Data Engineering.
- 📊 Passionate about **data visualization** and **API development**.
- 🔍 Exploring **LangChain** for AI-powered resume interaction.
""")

# Resume Download
resume_path = "assets/resumes/CharlesGeorge_Resume-DG-20250304.pdf"
if os.path.exists(resume_path):
    with open(resume_path, "rb") as resume_file:
        resume_bytes = resume_file.read()
    col1.download_button("📄 Download My Resume", resume_bytes, file_name="CharlesGeorge-Resume.pdf", mime="application/pdf")

col2.image("assets/images/The Data Vault - Placeholder banner.webp", width=400)  # Placeholder image

st.markdown("---")
st.markdown("💻 Built with Streamlit | 🚀 Hosted via GitHub & Streamlit Community Cloud")
