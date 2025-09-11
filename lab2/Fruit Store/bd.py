import sqlite3
try:

    dbcon=sqlite3.connect("temp.db")
    print("Database opened successfully")

except sqlite3.Error as e:
    print("Error in opening database:", e)
    print(e)

# table create 

tbl_create="create table if not exists fruit_stock (fruit_name text primary key, price real, quantity integer)"
try:

    dbcon.execute(tbl_create)
    print("Table created successfully")
except sqlite3.Error as e:
    print(e)
    



