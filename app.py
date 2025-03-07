import os
import streamlit as st
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Home", page_icon="💻", layout="wide")

Navbar()

# Logo
# HORIZONTAL_BLUE = "assets/images/RR_Logo.svg"
# HORIZONTAL_WHITE = "assets/images/RR_Logo_dm.svg"

# st.logo(HORIZONTAL_BLUE, icon_image=HORIZONTAL_WHITE)

# Page Content
st.title("Welcome to My Data Vault 👋")
st.write("\n")

col1, col2 = st.columns([2, 1])
col1.markdown("""
## 🚀 About This Project
The Data Vault is my **self-built, interactive tech portfolio**, designed to **showcase my expertise** in data science development, data engineering, and data visualization.

Every component of this application has been **individually crafted**, from the **frontend interface** in Streamlit to the **backend services** powered by FastAPI, LangChain, and database integrations. This project is more than just a resume—it's a **technical demonstration of my skills in real-world application development**.

## 🎯 Why This Matters
Rather than a static resume, this project provides a **live demonstration** of my **technical ability**, engineering mindset, and problem-solving skills. You can interact with my experience visually, explore my skills dynamically, and even **query my resume** and chat with my experience using an AI-powered interface.

## 📌 How I'm Tracking Progress
This project follows an organized development lifecycle:
- **🔄 Version Control:** Managed with GitHub for tracking changes & iterations.
- **📋 Milestones & Issues:** Each feature is documented & tracked using **GitHub Issues & Milestones**.
- **🛠️ Agile Development:** Continuous improvements based on structured phases.

You can explore the full **development history, commits, and planned milestones** in my [GitHub repository](https://github.com/87designer/the-data-vault).
              
---
💡 **Want to learn more?** Click through the navigation to explore my journey!
""")
# ## 🔧 Technologies & Skills
# - **Frontend:** Streamlit for UI/UX, interactive dashboards, and real-time querying.
# - **Backend:** FastAPI for API development, handling data dynamically.
# - **Data Visualization:** Plotly for engaging data-driven insights.
# - **Machine Learning & AI:** LangChain-powered retrieval system for querying my experience dynamically.
# - **Deployment & DevOps:** CI/CD automation with GitHub Actions, cloud deployment.


col2.image("assets/images/The Data Vault - Placeholder banner.webp", width=400)  # Placeholder image

# Resume Download
resume_path = "assets/resumes/CharlesGeorge_Resume-DG-20250304.pdf"
if os.path.exists(resume_path):
    with open(resume_path, "rb") as resume_file:
        resume_bytes = resume_file.read()
    col2.download_button("📄 Download My Resume", resume_bytes, file_name="CharlesGeorge-Resume.pdf", mime="application/pdf")


st.markdown("---")
st.markdown("💻 Built with Streamlit | 🚀 Hosted via GitHub & Streamlit Community Cloud")
