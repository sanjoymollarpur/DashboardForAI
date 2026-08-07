import sqlite3
import os 

file_path="bank_ai1.db"
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"{file_path} deleted successfully.")
# else:
#     print(f"{file_path} does not exist.")


conn = sqlite3.connect(file_path)
cursor = conn.cursor()


employees =  [("Sanjoy", "AI", 85000)]
    



cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_table1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            project_name TEXT,
            project_description TEXT,
            project_state TEXT,
            department TEXT,
            problem TEXT
    )
    """)


def add_value(values1):
        
    cursor.executemany(
        "INSERT INTO user_table1 (user_name, project_name, project_description, project_state, department, problem) VALUES (?, ?, ?, ?, ?, ?)",
        values1
    )
    conn.commit()

def delete_project(p):
    # conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query=f"DELETE FROM user_table1 WHERE id='{p[0]}' and project_name = '{p[1]}'"
    cursor.execute(query)
    conn.commit()

def get_project(project_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id,
               user_name,
               project_name,
               project_description,
               project_state,
               department,
               problem
        FROM user_table1
        WHERE id = ?
    """, (project_id,))

    project = cursor.fetchone()

    conn.commit()

    return project
    
def update_project(project_id, project_name, description, status, department, problem):
    # conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE user_table1
        SET project_name = ?, project_description = ?, project_state = ?, department = ?,  problem = ?
        WHERE id = ?
    """, (project_name, description, status, department, problem, project_id))

    conn.commit()
    # conn.close()