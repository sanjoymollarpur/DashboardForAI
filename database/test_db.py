from user_db import add_value
import sqlite3

file_path="bank_ai1.db"


conn = sqlite3.connect(file_path)
cursor = conn.cursor()

employees1 =  [("user2","project name2", "project desc2", "ABC2", "IT2", "78000")]

add_value(employees1)
cursor.execute("SELECT * FROM user_table1")
print(cursor.fetchall())

