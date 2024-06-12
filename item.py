import sqlite3
from database import create_connection

class Item:
    def __init__(self, name, barcode, size, weight, vendor):
        self.name = name
        self.barcode = barcode
        self.size = size
        self.weight = weight
        self.vendor = vendor

    def save_to_db(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO inventory (name, barcode, size, weight, vendor)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.name, self.barcode, self.size, self.weight, self.vendor))
        conn.commit()
        conn.close()

    @staticmethod
    def fetch_all():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM inventory')
        items = cursor.fetchall()
        conn.close()
        return items
