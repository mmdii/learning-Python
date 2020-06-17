import sqlite3

dbc = sqlite3.connect("students_records.db")
cursor = dbc.cursor()

query = "SELECT DISTINCT NAMES FROM students"
cursor.execute(query)

name_of_stu = cursor.fetchall()

for names in name_of_stu:
    print(names)

dbc.commit()
dbc.close()