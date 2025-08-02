
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
def add_maintenance(device_id, date, description):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO maintenance (device_id, date, description)
            VALUES (?, ?, ?)
        ''', (device_id, date, description))
        conn.commit()
        print("✅ Maintenance enregistrée avec succès.")
    except sqlite3.IntegrityError:
        print("❌ Erreur : l'ID de l'appareil n'existe pas.")
    finally:
        conn.close()
def add_device(device_type, brand, serial_number, employee_id=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO devices (type, brand, serial_number, employee_id)
            VALUES (?, ?, ?, ?)
        ''', (device_type, brand, serial_number, employee_id))
        conn.commit()
        print("✅ Appareil ajouté avec succès.")
    except sqlite3.IntegrityError:
        print("❌ Erreur : numéro de série déjà utilisé ou ID employé invalide.")
    finally:
        conn.close()