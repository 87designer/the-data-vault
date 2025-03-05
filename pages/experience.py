import streamlit as st
import plotly.graph_objects as go
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Experience", page_icon="💼", layout="wide")

Navbar()

# Page Content
st.title("💼 Experience")

col1, col2 = st.columns([1,1])

col1.markdown("""#### Management Analyst | *2024 - Present*
**National Heart, Lung, and Blood Institute (HHS>NIH>NHLBI)**
- Developed and optimized large-scale data pipelines for workforce and budget analytics, improving efficiency and reducing processing time.
- Built machine learning models to enhance workforce planning accuracy, increasing position categorization precision by 15% and automating salary ceiling analysis.
- Designed and deployed API-driven geospatial analysis tools, cutting down processing time from 30 hours to under 15 minutes by optimizing data retrieval and API interactions.
- Created dynamic dashboards and visualizations for leadership, facilitating strategic decision-making in workforce planning and budgeting.

#### Data Scientist | *2020 - 2024*
**ECS Federal (ASGN>ECS)**
- Built a Python-powered AI-driven financial forecasting tool, reducing budget analysis turnaround from 6–8 weeks to under a week.
- Led NLP initiatives to automate grant text analysis, streamlining research funding evaluations.
- Developed automated workforce analytics dashboards, transforming raw data into interactive, real-time insights for leadership.
- Engineered a scalable API framework to support data-driven decision-making across multiple NIH divisions.

#### Database Admin / Analyst | *2019 - 2020*
**American Media Source**
- Managed relational databases
- Automated ETL processes
- Migrated data to Google Cloud.

#### Digital Marketing Data Analyst | *2018 - 2019*
**American Target Advertising**
- Led data-driven campaign analysis
- Developed SQL-based segmentation models

#### Property Management Analyst | *2012 - 2018*
**FFC Properties LLC**
- Built operational databases and analytics tools for property tracking.
""")


# Define hierarchy: Space → Roles → Job Titles →
labels = ["Data",
          "Analysis", "Science", "Engineering",  # First Level: Roles
          "Property Management Analyst", "Digital Marketing Data Analyst", "Database Admin / Analyst", "Data Scientist", "Management Analyst"  # Second Level: Job Titles
          ]

# Define parent-child relationships
parents = [
    "",  
    "Data", "Data", "Data", # Top-level nodes (Roles)
    "Analysis", "Analysis", "Engineering", "Science", "Analysis"  # Job Titles under Roles
    ]

# Define experience duration (years)
values = [
    13, # Total Years
    8, 4, 1,  # Years in each role category
    6, 1, 1, 4, 1,  # Years in each job title
    ]

# Define custom colors
custom_colors = {
    "Data": "",
    "Engineering": "#FF7F0E",  # Orange
    "Science": "#1F77B4",  # Blue
    "Analysis": "#2CA02C",  # Green
    "Database Admin / Analyst": "#FFB85F",  # Lighter Orange
    "Data Scientist": "#A6CEE3",  # Lighter Blue
    "Management Analyst": "#98DF8A",  # Lighter Green
    "Data Analyst": "#98DF8A",  # Lighter Green
}

fig =go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    marker=dict(colors=[custom_colors[label] for label in labels]),
))

fig.update_layout(
    # title_text="Years in Role",
    margin = dict(t=0, l=0, r=0, b=0)
    )

col2.plotly_chart(fig)