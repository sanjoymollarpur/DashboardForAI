import streamlit as st
from database.db import login_user

def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, role = login_user(username, password)

        if success:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Username or Password")
