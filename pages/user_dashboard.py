import streamlit as st
import sqlite3
from database.user_db import add_value
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

    if st.session_state.action == "update":
        st.write("Update form")

    elif st.session_state.action == "delete":
        st.write("Delete form")

    elif st.session_state.action == "add" and st.session_state.show_form:
        st.write("Add form")
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

    
    # if st.session_state.action == "update":
    #     with st.form("update_form"):
    #         record_id = st.number_input("Record ID", min_value=1)
    #         project_name = st.text_input("Project Name")
    #         project_description = st.text_area("Project Description")
    #         project_state = st.selectbox(
    #             "Project State",
    #             ["POC", "Pilot", "Developed"]
    #         )
    #         department = st.text_input("Department")
    #         problem = st.text_area("Problem")
    #         submit = st.form_submit_button("Update")
    #         if submit:
    #             update_value(
    #                 record_id,
    #                 project_name,
    #                 project_description,
    #                 project_state,
    #                 department,
    #                 problem
    #             )
    #             st.success("Project updated successfully!")
    #             st.session_state.action = None
    #             st.rerun()
    
    # with col1:
    #     add = st.button("➕ Add", width="stretch")

    # with col2:
    #     update = st.button("✏️ Update", width="stretch")

    # with col3:
    #     delete = st.button("🗑️ Delete", width="stretch")

    # st.write(df)
    # print(rows)

    # st.title("Project Registration")

    # with st.form("project_form"):

    #     case_id = st.text_input("Case ID")

    #     project_name = st.text_input("Project Name")

    #     project_description = st.text_area(
    #         "Project Description",
    #         height=120
    #     )

    #     project_state = st.selectbox(
    #         "Project State",
    #         ["POC", "Pilot", "Developed"]
    #     )

    #     department = st.text_input("Department")

    #     problem = st.text_area(
    #         "Problem Statement",
    #         height=100
    #     )

    #     document = st.file_uploader(
    #         "Attach Document",
    #         type=["pdf", "docx", "doc", "xlsx", "xls", "pptx", "txt"]
    #     )

    #     submitted = st.form_submit_button("Submit")

    # if submitted:
    #     st.success("Project submitted successfully!")

    #     st.write("### Submitted Details")
    #     st.write(f"**Case ID:** {case_id}")
    #     st.write(f"**Project Name:** {project_name}")
    #     st.write(f"**Project Description:** {project_description}")
    #     st.write(f"**Project State:** {project_state}")
    #     st.write(f"**Department:** {department}")
    #     st.write(f"**Problem Statement:** {problem}")

    #     if document is not None:
    #         st.write(f"**Uploaded File:** {document.name}")