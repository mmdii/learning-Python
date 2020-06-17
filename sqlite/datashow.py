import sqlite3

con = sqlite3.connect("students_records.db")
cursor = con.cursor()

query = """SELECT * FROM students """
cursor.execute(query)

names_of_students = cursor.fetchall()

for id,names,marks,grades in names_of_students:
    print(id,names, marks, grades)

con.close()