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
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    salary REAL
)
""")

def add_value(values1):
        
    cursor.executemany(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        values1
    )
    conn.commit()

# add_value(employees)
# cursor.execute("SELECT * FROM employees")
# print(cursor.fetchall())