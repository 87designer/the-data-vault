import streamlit as st
from modules.nav import Navbar


# Set up Streamlit page configuration
st.set_page_config(page_title="My Data Vault - Projects", page_icon="📂", layout="wide")

Navbar()

# Page Content
st.title("📂 Projects")
st.markdown("""You’ve just landed on my **latest project**—this very App! 🎉 Like everything else here, it’s a **work in progress**, evolving as I learn, build, and refine.

Some projects are polished and battle-tested, while others are still in the tinkering phase, constantly improving with new insights and iterations. The goal? Keep building, **keep learning, and keep leveling up**.

So, take a look around—there’s a mix of **finished tools, ongoing experiments, and ideas still taking shape**. Who knows? By the time you check back, this page might have leveled up too.

🔧 **Build. Break. Improve. Repeat.**""")


# Custom CSS for Larger Expander Titles
st.markdown("""
    <style>
        .st-emotion-cache-89jlt8 {
            font-size: 18px !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)


# Sample project data - Replace with dynamic API data in Phase 3
projects = [
    {"name": "ResumeReactor: Powering Seamless Career Transitions 🚀", "live_demo": "https://resume-reactor.streamlit.app/", "github_link": "https://github.com/87designer/resume-reactor", "description": """Making the leap from **federal employment to the private sector**? **ResumeReactor** streamlines the process by transforming **long, detailed federal resumes** into **concise, ATS-optimized** industry resumes—helping professionals **stand out** in competitive job markets.

- 🔹 **AI-Powered Resume Optimization** – Tailors resumes to match job descriptions.
- 🔹 **ATS-Friendly Formatting** – Ensures clear structure, quantifiable achievements, and proper keyword alignment.
- 🔹 **Industry-Specific Adjustments** – Adapts resumes for IT, Finance, Healthcare, and more.
- 🔹 **Effortless Resume Generation** – Upload your resume, paste a job description, and generate a polished document in seconds.
- 🔹 **One-Click Download** – Get your resume in a ready-to-submit Word format.

Built with **Streamlit, Python, and OpenAI’s GPT-4**, ResumeReactor is designed for **career changers, federal employees, and job seekers** looking to break into private industry with a resume that **gets results**.

📄 **Faster Applications. Stronger Resumes. Better Opportunities.**"""},
    {"name": "Data Science Leadership Kit: Leading with Insight & Impact", "live_demo": None, "github_link": "https://github.com/87designer/DS-Leadership-Kit", "description": """Great leadership isn’t just about authority—it’s about **influence, strategy, and fostering a culture of excellence**. This **Data Science Leadership Kit** is a growing collection of **lessons learned, best practices, and practical tools** that I’ve gathered throughout my journey, with the goal of empowering both myself and others to lead effectively—whether from the front or from any seat at the table.

- 🔹 **Guides for fostering a strong data-driven culture**
- 🔹 **Best practices for collaboration, communication, and decision-making**
- 🔹 **Strategies for mentoring, coaching, and technical leadership**
- 🔹 **Templates, frameworks, and checklists for leading data science initiatives**

This kit is not just a resource—it’s a **foundation for future leadership**, designed to help navigate the challenges of managing data teams, driving impactful projects, and promoting good practices that elevate the entire field.

💡 **Leadership isn’t a title—it’s a mindset. Let’s build better teams, one insight at a time.**"""},
    {"name": "Advent of Code: The Holiday Hustle Edition 🎄💻", "live_demo": None, "github_link": "https://github.com/87designer/advent_of_code", "description": """The holiday season is a whirlwind of **festivities, family time, and last-minute gift shopping**—but that doesn’t stop me from tackling as many **Advent of Code** challenges as possible!

Each December, I try to dive into these **algorithmic puzzles**, balancing **coding, holiday chaos, and keeping the tree upright**. While I may not complete every problem before the cookies run out, this repo showcases:

- 🎁 **Solutions in Python**
- 🎄 **Optimized & evolving approaches**
- 📄 **High Quality & Readable Solutions over Complex ones**
- 🎅 **Attempts to squeeze in coding between holiday madness**

Some days I power through, other days the **holiday spirit wins**—but that’s part of the fun!

**‘Tis the season for code, cookies, and compromised sleep schedules.**"""},
    {"name": "AWB0412 LogShield", "live_demo": None, "github_link": "https://github.com/87designer/arduino_wifi_button", "description": """What if a simple button press could track the moments that matter? Inspired by a social media ad and fueled by newfound electronics skills, I set out to build a **WiFi-enabled event logging device**—but instead of buying one, I made my own.

The **AWB0412 LogShield** is an Arduino-based **categorical data logging shield** that captures real-world events at the press of a button. **Whether it's tracking infant care, logging productivity, or monitoring personal habits**, this device seamlessly transmits timestamped events to Google Sheets via WiFi.
     
Featuring **four tactile buttons** with **single, double, and hold-click actions**, it provides **12 unique event inputs**—all in a compact, programmable shield. A **multicolor LED** provides instant feedback, ensuring seamless operation.
     
This project showcases **hardware design (EDA, PCB prototyping), firmware development (C++), and cloud integration (Google Apps Script)**—bridging physical interaction with digital record-keeping.
     
**Why Buy It When You Can Build It?**
     
From initial concept to PCB fabrication, this project brings together **DIY electronics, cloud automation, and practical real-world applications**.
    
🔹 **Press. Log. Automate.** 🔹"""},
    {"name": "SchoolDays Tracker: A Smarter Way to Plan Your Homeschool Year", "live_demo": "https://schooldayscalculator.streamlit.app/", "github_link": "https://github.com/87designer/school-days-calculator", "description": """Keeping track of school days shouldn't be a headache. **SchoolDays Tracker** is a **simple yet powerful homeschool calendar calculator** that helps parents and educators efficiently plan and manage their school year.

Built with **Python and Streamlit**, and deployed with **CI/CD principles via GitHub and Streamlit Community Cloud**, this app streamlines the process of:

- ✅ **Tracking completed and remaining school days**
- ✅ **Customizing school year schedules**
- ✅ **Factoring in holidays, breaks, and learning days**
- ✅ **Ensuring compliance with homeschooling requirements**

Whether you're structuring a full academic year or planning as you go, **SchoolDays Tracker** keeps you on top of your progress with ease.

📅 **Smart planning. Less stress. More learning.**"""},
    {"name": "Codewars", "live_demo": None, "github_link": "https://github.com/87designer/Codewars/tree/main", "description": """Sharpening coding skills is a never-ending battle, and **CodeWars** is the ultimate dojo. This repository is my personal archive of **solutions, strategies, and optimizations** for a wide range of challenges from CodeWars.com."""}
]

# Display projects in expandable sections
for project in projects:
    with st.expander(project['name']):
        st.markdown(project["description"])
        if project['live_demo']:
            st.markdown(f"[🌐 Live Demo]({project['live_demo']}) | [🔗 View on GitHub]({project['github_link']})")
        else:
            st.markdown(f"[🔗 View on GitHub]({project['github_link']})")