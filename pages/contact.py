import streamlit as st
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Get in Touch", page_icon="📬", layout="wide")

Navbar()

# Page Content
st.title("📬 Get in Touch")
st.markdown("""
I’d love to connect! Whether you have questions, collaboration ideas, or just want to chat about tech, feel free to reach out through any of the platforms below.

📬 **Email:** [cgdesigned@gmail.com](mailto:cgdesigned@gmail.com)  
💼 **LinkedIn:** [in/charlesgcv](https://www.linkedin.com/in/charlesgcv/)  
🐙 **GitHub:** [@87designer](https://github.com/87designer)  
🌐 **Website/Portfolio:** [charlesgeorge.dev/](https://www.charlesgeorge.dev/)

I’m always open to discussions on software development, data engineering, AI, and anything tech-related. Let’s connect! 🚀
""")
