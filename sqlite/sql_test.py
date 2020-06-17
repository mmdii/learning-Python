import sqlite3
try:
    dbase = sqlite3.connect("students_records.db")
    dbase.execute('''CREATE TABLE students(ID INT PRIMARY KEY NOT NULL,NAMES TEXT NOT NULL,MARKS TEXT NOT NULL,GRADES TEXT NOT NULL)''')
    dbase.close()
except:
    print("Connection Error")