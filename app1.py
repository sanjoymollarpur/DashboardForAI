import streamlit as st
# from database import init_db
# from auth import check_login, logout

# # Import Pages
# from pages.login import login_page
# from pages.admin_dashboard import admin_dashboard
# from pages.owner_dashboard import owner_dashboard

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="AI Governance Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# Initialize Database
# -----------------------------------------------------
# init_db()

# -----------------------------------------------------
# Session Variables
# -----------------------------------------------------
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if "username" not in st.session_state:
#     st.session_state.username = ""

# if "role" not in st.session_state:
#     st.session_state.role = ""

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------
def sidebar():

    with st.sidebar:

        st.title("🤖 AI Governance")

        st.markdown("---")

        st.write(f"**User:** {st.session_state.username}")
        st.write(f"**Role:** {st.session_state.role}")

        st.markdown("---")

        if st.button("Logout", use_container_width=True):
            logout()

# -----------------------------------------------------
# Main Routing
# -----------------------------------------------------

def main():

    if not check_login():

        login_page()

    # else:

    # sidebar()

        # if st.session_state.role == "Admin":

        #     admin_dashboard()

        # elif st.session_state.role == "Owner":

        #     owner_dashboard()

        # else:

        #     st.error("Unknown User Role")

if __name__ == "__main__":
    main()


