# models/customer.py

import mysql.connector
from db_connection import get_connection
from models.user import User

class Customer(User):
    def __init__(self, name, email, password, balance=0.0):
        super().__init__(name, email, password)
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def view_balance(self):
        print(f"Your current balance is: ₹{self.__balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            self.__balance += amount
            self.update_balance()
            print(f"₹{amount:.2f} deposited successfully.")
        except ValueError:
            print("Invalid amount entered.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            if amount > self.__balance:
                print("Insufficient balance.")
                return
            self.__balance -= amount
            self.update_balance()
            print(f"₹{amount:.2f} withdrawn successfully.")
        except ValueError:
            print("Invalid amount entered.")

    def update_balance(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE customers SET balance = %s WHERE email = %s", (self.__balance, self.email))
            conn.commit()
        except mysql.connector.Error as e:
            print("Database error:", e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def register():
        print("\n--- Customer Registration ---")
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
            if cursor.fetchone():
                print("Email already exists.")
                return
            cursor.execute("INSERT INTO customers (name, email, password, balance) VALUES (%s, %s, %s, %s)",
                           (name, email, password, 0.0))
            conn.commit()
            print("Customer registered successfully.")
        except mysql.connector.Error as e:
            print("Database error:", e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def login():
        print("\n--- Customer Login ---")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE email = %s AND password = %s", (email, password))
            row = cursor.fetchone()
            if row:
                print(f"Welcome {row[1]}!")
                return Customer(row[1], row[2], row[3], row[4])
            else:
                print("Invalid credentials.")
                return None
        except mysql.connector.Error as e:
            print("Database error:", e)
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_all_customers():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email FROM customers")
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print("Database error:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_customer(cust_id, name, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE customers SET name = %s, email = %s WHERE id = %s", (name, email, cust_id))
            conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            print("Database error:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_customer(cust_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM customers WHERE id = %s", (cust_id,))
            conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            print("Database error:", e)
            return False
        finally:
            cursor.close()
            conn.close()
