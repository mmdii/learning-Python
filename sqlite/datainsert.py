import sqlite3

con = sqlite3.connect("students_records.db")
cursor = con.cursor()
cursor.execute("""INSERT INTO students(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",(2,"javad","1200","A"))
con.commit()

con.close()