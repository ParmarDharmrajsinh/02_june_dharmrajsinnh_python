# db_connection.py

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Change this to your MySQL username
        password="",         # Add your password here
        database="bank_db"   # Your database name
    )
