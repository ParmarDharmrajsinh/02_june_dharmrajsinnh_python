#22) Write a Python program to insert data into an SQLite3 database and fetch it.


import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

students_data = [
    ('Dharmraj', 22, 'A'),
    ('Parmar', 21, 'B'),
    ('Ravi', 23, 'A'),
]

cursor.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', students_data)
print("Data inserted successfully!")

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

print("\nData in the 'students' table:")
for row in rows:
    print(row)
conn.close()
