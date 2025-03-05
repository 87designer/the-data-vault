import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Skills", page_icon="🛠️", layout="wide")

Navbar()

# Page Content
st.title("🛠️ Skills & Technologies")

# Sample skills data (To be replaced with dynamic API data in Phase 3)
skills = {
    "Data Science & Machine Learning": ["DataCleaning", "DataAnalysis", "DataManagement", "DataVisualization", 
                                        "JupyterHub", "JupyterLab", "JupyterNotebook", "AzureDataStudio", "FeatureEngineering",
                                        "PDF-Scraping", "Web-Scraping", "Pandas", "Numpy", "Scikit-Learn", "Statsmodels", "SciPy", "XLSXWriter", "Selenium"],
    "Data Visualization": ["PowerBI", "LookerStudio", "QlikSense", "Plotly", "Dash", "Streamlit", "Matplotlib", "Seaborn"],
    "Programming / Scripting": ["Python", "HTML", "CSS", "PostgreSQL", "MySQL", "Oracle", "NoSQL", "FastAPI", "REST-APIs", "GitHub"],
    "Cloud Familiarity": ["AWS", "Azure", "GCP"],
    "Business & Productivity": ["Excel", "PowerAutomate", "Visio", "SharePoint"]
}


# Multi-Select for Skill Categories
# st.subheader("📊 Filter Skills by Category:")
selected_categories = st.multiselect("", list(skills.keys()), default=list(skills.keys())) # Select categories:

# Display selected skills
if selected_categories:
    # st.subheader("📌 Selected Skills")
    for category in selected_categories:
        with st.expander(f"**{category}**"):
            st.write("\n".join([f"- {skill}" for skill in skills[category]]))
    
    # Generate word cloud for selected skills
    selected_skills = [skill for cat in selected_categories for skill in skills[cat]]
    skills_text = " ".join(selected_skills)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(skills_text)

    # Display word cloud
    st.subheader("🔹 Skills Word Cloud")
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.write("Select one or more categories to view skills and generate a word cloud.")
