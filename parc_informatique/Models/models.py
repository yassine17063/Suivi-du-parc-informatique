
import sqlite3

DB_PATH = "parc_informatique.db"

def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# ------------ Employees ------------

def add_employee(emp_id, name, department):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO employees (id, name, department) VALUES (?, ?, ?)",
        (emp_id, name, department)
    )
    conn.commit()
    conn.close()


def list_employees(return_data=False):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, department FROM employees ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    if return_data:
        return rows
    if rows:
        for r in rows:
            print(f"ID: {r[0]} | Nom: {r[1]} | Département: {r[2]}")
    else:
        print("Aucun employé.")

def delete_employee(employee_id):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    conn.commit()
    conn.close()

def modify_employee_department(employee_id, new_department):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE employees SET department = ? WHERE id = ?", (new_department, employee_id))
    conn.commit()
    conn.close()

# ------------ Devices ------------

def add_device(device_type, brand, serial_number, employee_id=None):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO devices (type, brand, serial_number, employee_id) VALUES (?, ?, ?, ?)",
        (device_type, brand, serial_number, employee_id),
    )
    conn.commit()
    conn.close()

def list_devices(return_data=False):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, type, brand, serial_number, employee_id FROM devices ORDER BY id"
    )
    rows = cur.fetchall()
    conn.close()
    if return_data:
        return rows
    if rows:
        for d in rows:
            print(
                f"ID: {d[0]} | Type: {d[1]} | Marque: {d[2]} | N° Série: {d[3]} | Employé ID: {d[4] if d[4] is not None else '—'}"
            )
    else:
        print("Aucun appareil.")

def delete_device(device_id):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM devices WHERE id = ?", (device_id,))
    conn.commit()
    conn.close()

# ------------ Maintenance ------------

def add_maintenance(device_id, date, description):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO maintenance (device_id, date, description) VALUES (?, ?, ?)",
        (device_id, date, description),
    )
    conn.commit()
    conn.close()

def list_maintenance_by_device(device_id, return_data=False):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, device_id, date, description FROM maintenance WHERE device_id = ? ORDER BY date DESC, id DESC",
        (device_id,),
    )
    rows = cur.fetchall()
    conn.close()
    if return_data:
        return rows
    if rows:
        for m in rows:
            print(f"ID: {m[0]} | Appareil: {m[1]} | Date: {m[2]} | {m[3] or ''}")
    else:
        print("Aucune maintenance pour cet appareil.")
