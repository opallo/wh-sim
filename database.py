import sqlite3

def create_connection():
    conn = sqlite3.connect('warehouse.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            barcode TEXT NOT NULL,
            size TEXT NOT NULL,
            weight TEXT NOT NULL,
            vendor TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
