import streamlit as st
import sqlite3
from database.user_db import add_value
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

    