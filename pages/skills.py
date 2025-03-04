import streamlit as st
import pandas as pd
import plotly.express as px
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Skills", page_icon="📞", layout="wide")

Navbar()

# Skills Page
st.title("🛠️ Skills & Technologies")
st.markdown("A breakdown of my tech stack and proficiency.")
