import streamlit as st
import sqlite3
from database.user_db import add_value, delete_project
import pandas as pd


def user_dashboard(user):
    st.title("User Dashboard")
    st.write(user)

    file_path="bank_ai1.db"
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    query=f"SELECT * FROM user_table1 WHERE user_name='{user}'"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(
    rows,
    columns=["id", "user_name", "project_name", "project_description", "project_state", "department", "problem"]
    )
    st.dataframe(df, width="stretch")

    col1, col2, col3 = st.columns(3)

    if "action" not in st.session_state:
        st.session_state.action = None
    
    if "show_form" not in st.session_state:
        st.session_state.show_form = False

    with col1:
        if st.button("➕ Add", width="stretch"):
            st.session_state.action = "add"
            st.session_state.show_form = True

    with col2:
        if st.button("✏️ Update", width="stretch"):
            st.session_state.action = "update"

    with col3:
        if st.button("🗑 Delete", width="stretch"):
            st.session_state.action = "delete"
            st.session_state.show_form = True

    if st.session_state.action == "update":
        st.write("Update form")

    elif st.session_state.action == "delete" and st.session_state.show_form:
        st.subheader("Delete Project")
        projects=rows
        if not projects:
            st.info("No projects found.")
        else:
            project_names = [(p[0],p[2]) for p in projects]   # Adjust index as needed
            selected_project = st.selectbox(
                "Select Project",
                project_names
            )
            # st.write(project_name)
            with st.form("delete_form"):
                confirm = st.checkbox(
                    "I confirm that I want to delete this project."
                )
                submit = st.form_submit_button("Delete")

                if submit:
                    if confirm:
                        delete_project(selected_project)   # Your delete function
                        conn.close()
                        st.success("Project deleted successfully!")

                        st.session_state.action = None
                        st.rerun()
                    else:
                        st.warning("Please confirm before deleting.")
    elif st.session_state.action == "add" and st.session_state.show_form:
        with st.form("project_form"):
            user_name = user
            project_name = st.text_input("Project Name")
            project_description = st.text_area("Project Description")
            project_state = st.selectbox(
                "Project State",
                ["POC", "Pilot", "Deployed"]
            )
            department = st.text_input("Department")
            problem = st.text_area("Problem")

            submit = st.form_submit_button("Save")

            if submit:
                employees1 =  [(user_name,project_name, project_description, project_state, department, problem)]
                add_value(employees1)
                st.success("Project added successfully!")
                # Hide the form after saving (optional)
                st.session_state.show_form = False
                st.rerun()

    