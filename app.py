import streamlit as st

from pages.login import login_page
from pages.admin_dashboard import admin_dashboard
from pages.user_dashboard import user_dashboard


def main():
    st.set_page_config(
        page_title="AI Governance Dashboard",
        page_icon="🤖",
        layout="wide"
    )

    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "role" not in st.session_state:
        st.session_state.role = None

    if "username" not in st.session_state:
        st.session_state.username = None

    # Show login page
    if not st.session_state.logged_in:
        login_page()
        return

    # Sidebar
    with st.sidebar:
        st.title("AI Dashboard")
        st.write(f"Welcome **{st.session_state.username}**")
        st.write(f"Role : **{st.session_state.role}**")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.role = None
            st.session_state.username = None
            st.rerun()

    # Route dashboard
    if st.session_state.role == "admin":
        admin_dashboard()

    elif st.session_state.role[:4] == "user":
        # print(st.session_state.role[:3])
        user_dashboard(st.session_state.role)

    else:
        st.error("Invalid user role.")


if __name__ == "__main__":
    main()