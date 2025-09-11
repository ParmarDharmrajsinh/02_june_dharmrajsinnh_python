# models/banker.py

import mysql.connector
from db_connection import get_connection
from models.user import User

class Banker(User):
    def register(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bankers WHERE email = %s", (self.email,))
            if cursor.fetchone():
                return False

            cursor.execute("INSERT INTO bankers (name, email, password) VALUES (%s, %s, %s)",
                           (self.name, self.email, self.password))
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Database error:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def login(email, password):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bankers WHERE email = %s AND password = %s", (email.strip(), password.strip()))
            row = cursor.fetchone()
            if row:
                return Banker(row[1], row[2], row[3])
            return None
        except mysql.connector.Error as e:
            print("Database error:", e)
            return None
        finally:
            cursor.close()
            conn.close()
