import sqlite3

db = sqlite3.connect("students_records.db")
cursor = db.cursor()

query = "SELECT AVG(MARKS) FROM students"
cursor.execute(query)

avg_marks = cursor.fetchall()

for avg in avg_marks:
    print(avg)

db.commit()
db.close()