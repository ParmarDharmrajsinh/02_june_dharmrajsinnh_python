#Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data. 


import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute

cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", ("Dharmrajsinh", 22, "Python"))
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", ("Parth", 21, "Java"))
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", ("Krishna", 23, "Data Science"))
conn.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Student Records:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
conn.close()
