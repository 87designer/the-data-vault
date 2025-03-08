import streamlit as st
import requests
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Roadmap", page_icon="🚀", layout="wide")

Navbar()


# Roadmap Page
st.title("🚀 Roadmap")

st.markdown("""
This page provides an **up-to-date view** of what's next for this project, leveraging data directly from **GitHub Issues & Milestones**. Stay tuned for new features, improvements, and upcoming developments!
""")

# GitHub Repository Info (Update with your repo details)
GITHUB_USERNAME = "87designer"
GITHUB_REPO = "the-data-vault"
GITHUB_REPO_URL = "https://github.com/87designer/the-data-vault"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/milestones"
GITHUB_CLOSED_MILESTONES_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/milestones?state=closed"
GITHUB_ISSUES_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/issues"

# Fetch Milestones from GitHub API
try:
    response = requests.get(GITHUB_API_URL)
    milestones = response.json()
    
    response_closed = requests.get(GITHUB_CLOSED_MILESTONES_URL)
    closed_milestones = response_closed.json()
    
    if response.status_code == 200 and response_closed.status_code == 200:
        st.subheader("📌 Upcoming Milestones")
        for milestone in milestones:
            completed_issues = milestone['closed_issues']
            total_issues = milestone['open_issues'] + milestone['closed_issues']
            progress = (completed_issues / total_issues) if total_issues > 0 else 0
            
            # Fetch issues related to this milestone
            issues_response = requests.get(GITHUB_ISSUES_URL, params={"milestone": milestone["number"], "state": "open"})
            issues = issues_response.json() if issues_response.status_code == 200 else []
            
            with st.expander(f"{milestone['title']} (Due: {milestone['due_on'] if milestone['due_on'] else 'No Deadline'})"):
                st.markdown("##### 📌 Description")
                st.write(milestone['description'] if milestone['description'] else "No description available.")
                st.markdown("##### 📊 Progress")
                st.markdown("""<style>
                            .stProgress .st-fa {
                                background-color: green;
                            }
                            </style>""", unsafe_allow_html=True)
                st.progress(progress, text=f"{completed_issues} of {total_issues} tasks completed")
                st.markdown("##### 📋 Remaining Issues")
                if issues:
                    for issue in issues:
                        st.markdown(f"- [{issue['title']}]({issue['html_url']})")
                else:
                    st.write("No open issues remaining.")
        
        st.subheader("✅ Completed Milestones")
        for milestone in closed_milestones:
            with st.expander(f"{milestone['title']} (Completed)"):
                st.markdown("##### 📌 Description")
                st.write(milestone['description'] if milestone['description'] else "No description available.")
                st.write(f"🎉 All {milestone['closed_issues']} issues in this milestone have been successfully completed!")
    else:
        st.warning("No milestones found or unable to retrieve data.")
except Exception as e:
    st.error(f"Failed to load roadmap data: {e}")

st.markdown(f"""
---
🔄 This roadmap updates dynamically based on GitHub milestones and issue tracking.

🔗 [View the full project on GitHub]({GITHUB_REPO_URL})
""")
