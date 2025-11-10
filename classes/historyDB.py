import sqlite3
import json
from datetime import datetime

class HistoryDB:
    def __init__(self):
        self.conn = sqlite3.connect('history.db')
        self.create_table()

    def create_table(self):
        """Создаем одну таблицу для истории"""
        self.conn.execute('''CREATE TABLE IF NOT EXISTS history
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          formula_name TEXT,
                          inputs TEXT,
                          result TEXT,
                          timestamp TEXT)''')
        self.conn.commit()

    def add_calculation(self, formula_name, inputs, result):
        """Добавляем запись в историю"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        inputs_json = json.dumps(inputs)  # сохраняем как JSON

        self.conn.execute('INSERT INTO history (formula_name, inputs, result, timestamp) VALUES (?, ?, ?, ?)',
                          (formula_name, inputs_json, str(result), timestamp))
        self.conn.commit()

    def get_history(self):
        """Получаем всю историю"""
        cursor = self.conn.execute(
            'SELECT * FROM history ORDER BY timestamp DESC')
        return cursor.fetchall()

    def clear_history(self):
        """Очищаем историю"""
        self.conn.execute('DELETE FROM history')
        self.conn.commit()
