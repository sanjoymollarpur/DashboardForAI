import streamlit as st
import sqlite3
from database.user_db import add_value, delete_project, get_project, update_project
import pandas as pd

def admin_dashboard():
    st.title("Admin Dashboard")

    file_path="bank_ai1.db"
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    query=f"SELECT * FROM user_table1"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(
    rows,
    columns=["id", "user_name", "project_name", "project_description", "project_state", "department", "problem"]
    )
    st.dataframe(df, width="stretch")


    col2, col3 = st.columns(2)

    if "action" not in st.session_state:
        st.session_state.action = None
    
    if "show_form" not in st.session_state:
        st.session_state.show_form = False

    

    with col2:
        if st.button("✏️ Update", width="stretch"):
            st.session_state.action = "update"
            st.session_state.show_form = True

    with col3:
        if st.button("🗑 Delete", width="stretch"):
            st.session_state.action = "delete"
            st.session_state.show_form = True

    if st.session_state.action == "update" and st.session_state.show_form:
        st.subheader("Update Project")
        projects=rows
        if not projects:
            st.info("No projects found.")
        else:
            project_names = [(p[0],p[2]) for p in projects]   # Adjust index as needed
            selected_project = st.selectbox(
                "Select Project",
                project_names
            )
            project_id=selected_project[0]
            project = get_project(project_id)
            print(project)

            with st.form("update_form"):

                project_name = st.text_input(
                    "Project Name",
                    value=project[2]
                )

                project_description = st.text_area(
                    "Project Description",
                    value=project[3]
                )

                project_state = st.selectbox(
                    "Project State",
                    ["POC", "Pilot", "Deployed"],
                    index=["POC", "Pilot", "Deployed"].index(project[4])
                )

                department = st.text_input(
                    "Department",
                    value=project[5]
                )

                problem = st.text_area(
                    "Problem",
                    value=project[6]
                )

                submit = st.form_submit_button("Update")

                if submit:
                    update_project(
                        project_id,
                        project_name,
                        project_description,
                        project_state,
                        department,
                        problem
                    )
                    conn.close()
                    st.success("Project updated successfully!")
                    st.session_state.action = None
                    st.rerun()


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
    

    

