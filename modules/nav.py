import streamlit as st


def Navbar():
    with st.sidebar:
        st.sidebar.subheader("Navigation")
        st.page_link('app.py', label='Home', icon='💻')
        st.page_link('pages/experience.py', label='Experience', icon='💼')
        st.page_link('pages/skills.py', label='Skills', icon='🛠️')
        st.page_link('pages/projects.py', label='Projects', icon='📂')
        st.page_link('pages/contact.py', label='Get in Touch', icon='📬')
        st.page_link('pages/roadmap.py', label='Roadmap', icon='🚀')
        
        # st.sidebar.subheader("External Links")
        # st.page_link('https://github.com/87designer/the-data-vault', label='GitHub', icon='👨‍💻')
        # st.sidebar.markdown("🔒 Experience")
        # st.sidebar.markdown("🔒 Skills")
        # st.sidebar.markdown("🔒 Projects")
