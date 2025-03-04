import streamlit as st


def Navbar():
    with st.sidebar:
        st.sidebar.title("Navigation")
        st.page_link('app.py', label='Home', icon='💻')
        st.page_link('pages/contact.py', label='Contact', icon='📞')
        st.sidebar.markdown("🔒 Experience (Coming Soon)")
        st.sidebar.markdown("🔒 Skills (Coming Soon)")
        st.sidebar.markdown("🔒 Projects (Coming Soon)")