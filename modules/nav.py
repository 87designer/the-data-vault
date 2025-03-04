import streamlit as st


def Navbar():
    with st.sidebar:
        st.sidebar.subheader("Navigation")
        st.page_link('app.py', label='Home', icon='💻')
        st.page_link('https://github.com/87designer/the-data-vault', label='GitHub', icon='📁')
        st.page_link('pages/contact.py', label='Contact', icon='📞')
        st.sidebar.subheader("Coming Soon")
        st.sidebar.markdown("🔒 Experience")
        st.sidebar.markdown("🔒 Skills")
        st.sidebar.markdown("🔒 Projects")
