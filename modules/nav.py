import streamlit as st


def Navbar():
    with st.sidebar:
        st.sidebar.subheader("Navigation")
        st.page_link('app.py', label='Home', icon='💻')
        st.page_link('pages/experience.py', label='Experience', icon='💼')
        st.page_link('pages/skills.py', label='Skills', icon='🛠️')
        st.page_link('pages/contact.py', label='Contact', icon='📞')
        st.page_link('https://github.com/87designer/the-data-vault', label='GitHub', icon='📁')
        st.sidebar.subheader("Coming Soon")
        # st.sidebar.markdown("🔒 Experience")
        # st.sidebar.markdown("🔒 Skills")
        st.sidebar.markdown("🔒 Projects")
