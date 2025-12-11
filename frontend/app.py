import streamlit as st

st.set_page_config(
    page_title="Assignment Task Tracker",
    layout="wide"
)

# Initialize session state
if "token" not in st.session_state:
    st.session_state.token = None

# Main app logic
if st.session_state.token is None:
    st.title("Assignment Task Tracker")
    st.markdown("### A simple and effective way to manage your assignments and tasks")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### Features:
        - Track all your assignments in one place
        - Set due dates and monitor progress
        - Mark tasks as complete when finished
        - Secure authentication system
        """)
        
        st.info("This application was developed as a final project for ITCC14 Web Services.")

    with col2:
        st.markdown("### Get Started")
        st.write("Please login or register to continue.")
        
        col_login, col_register = st.columns(2)
        
        with col_login:
            if st.button("Login", use_container_width=True):
                st.switch_page("pages/Login.py")
        
        with col_register:
            if st.button("Register", use_container_width=True):
                st.switch_page("pages/Register.py")

    st.markdown("---")
    st.markdown("### Team Members")
    st.markdown("""
    - Mychal Redoblado (@Ka1ma) (MychalXU)
    - Kyle Gabriel T. Galanida (KGG-Student)
    - Karlos Semilla (@Ykarlossemilla)
    - Jhemar Visande (@JhemarVisande)
    """)
else:
    st.switch_page("pages/Tasks.py")
