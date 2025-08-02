
import sqlite3

DB_PATH = 'parc_informatique.db'

def add_employee(name, department):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, department) VALUES (?, ?)", (name, department))
    conn.commit()
    conn.close()
    print(f"Employé {name} ajouté.")

def list_employees():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    for emp in employees:
        print(emp)
