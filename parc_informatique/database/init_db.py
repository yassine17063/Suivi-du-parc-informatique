import sqlite3

def init_db():
    conn = sqlite3.connect('parc_informatique.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            brand TEXT,
            serial_number TEXT UNIQUE,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (device_id) REFERENCES devices(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Base de données initialisée.")

if __name__ == "__main__":
    init_db()
