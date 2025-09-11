import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3
from tkinter import messagebox
import random  

def create_patient_form():
    root = tk.Tk()
    root.title("Patient Registration Form")
    root.geometry("400x300")

    def get_datetime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_patient_id():
        return str(random.randint(10000, 99999))  

    ttk.Label(root, text="Patient ID:",font=35).grid(row=0, column=0, sticky='e')
    entry_id = ttk.Entry(root, width=30)
    entry_id.insert(0, generate_patient_id())  
    entry_id.grid(row=0, column=1)

    ttk.Label(root, text="Patient Name:",font=35).grid(row=1, column=0, sticky='e')
    entry_name = ttk.Entry(root, width=30)
    entry_name.grid(row=1, column=1)

    ttk.Label(root, text="City:",font=35).grid(row=2, column=0, sticky='e')
    city_names = ["rajkot", "jamnagar", "surat", "vadodra", "bhavnagar"]
    city_var = tk.StringVar()
    combo_city = ttk.Combobox(root, textvariable=city_var, values=city_names, width=28, state='readonly')
    combo_city.grid(row=2, column=1)

    ttk.Label(root, text="Date & Time:",font=35).grid(row=3, column=0, sticky='e')
    datetime_var = tk.StringVar(value=get_datetime())
    entry_datetime = ttk.Entry(root, textvariable=datetime_var, width=30)
    entry_datetime.grid(row=3, column=1)

    ttk.Label(root, text="Doctor Name:",font=35).grid(row=4, column=0, padx=10, pady=10, sticky='e')
    doctor_names = ["Dr. aadi", "Dr. nitin", "Dr. annirudhha", "Dr. mahek", "Dr. dharmmaraj","Dr. sanket"]
    doctor_var = tk.StringVar()
    combo_doctor = ttk.Combobox(root, textvariable=doctor_var, values=doctor_names, width=28, state='readonly')
    combo_doctor.grid(row=4, column=1)

    def submit_data():
        pid = entry_id.get()
        pname = entry_name.get()
        pcity = city_var.get()
        pdatetime = datetime_var.get()
        pdoctor = doctor_var.get()
        conn = sqlite3.connect('patient register.db')
        cur = conn.cursor()
        try:
            cur.execute("create table patient2(id text, name text, city text, datetime text, doctor text)")
            cur.execute("INSERT INTO patient2 (id, name, city, datetime, doctor) VALUES (?, ?, ?, ?, ?)",
                        (pid, pname, pcity, pdatetime, pdoctor))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success", "Patient data saved!")
        except Exception as e:
            tk.messagebox.showerror(e)

    submit_btn = ttk.Button(root, text="Submit", command=submit_data)
    submit_btn.grid(row=5, column=0, columnspan=2, pady=15)

    root.mainloop()
create_patient_form()