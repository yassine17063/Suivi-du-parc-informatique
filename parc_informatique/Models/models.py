
import sqlite3

DB_PATH = 'parc_informatique.db'

def add_employee(name, department):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, department) VALUES (?, ?)", (name, department))
    conn.commit()
    conn.close()
    print(f"Employé {name} ajouté.")
def delete_employee(employee_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Employé supprimé avec succès.")
        else:
            print("Aucun employé trouvé avec cet ID.")
    finally:
        conn.close()
def modify_employee_department(employee_id, new_department):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE employees SET department = ? WHERE id = ?",
            (new_department, employee_id)
        )
        conn.commit()
        if cursor.rowcount > 0:
            print(" Département mis à jour avec succès.")
        else:
            print(" Aucun employé trouvé avec cet ID.")
    finally:
        conn.close()

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
        print("Maintenance enregistrée avec succès.")
    except sqlite3.IntegrityError:
        print("Erreur : l'ID de l'appareil n'existe pas.")
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
        print("Appareil ajouté avec succès.")
    except sqlite3.IntegrityError:
        print("Erreur : numéro de série déjà utilisé ou ID employé invalide.")
    finally:
        conn.close()
def delete_device(device_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM devices WHERE id = ?", (device_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(" Appareil supprimé avec succès.")
        else:
            print(" Aucun appareil trouvé avec cet ID.")
    finally:
        conn.close()

def list_devices():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT d.id, d.type, d.brand, d.serial_number, e.name
        FROM devices d
        LEFT JOIN employees e ON d.employee_id = e.id
    ''')

    devices = cursor.fetchall()
    conn.close()

    if devices:
        print("\n📋 Liste des appareils :")
        for d in devices:
            device_id, type_, brand, serial, employee = d
            print(f"ID: {device_id} | Type: {type_} | Marque: {brand} | "
                  f"Série: {serial} | Employé: {employee if employee else 'Non affecté'}")
    else:
        print(" Aucun appareil trouvé.")
def list_maintenance_by_device(device_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT m.id, m.date, m.description
        FROM maintenance m
        WHERE m.device_id = ?
        ORDER BY m.date DESC
    ''', (device_id,))

    maintenances = cursor.fetchall()
    conn.close()

    if maintenances:
        print(f"\n Historique des maintenances pour l'appareil ID {device_id} :")
        for m in maintenances:
            maint_id, date, description = m
            print(f"- ID: {maint_id} | Date: {date} | Description: {description}")
    else:
        print(f" Aucune maintenance trouvée pour l'appareil ID {device_id}.")
