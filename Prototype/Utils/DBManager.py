import sqlite3

class DBManager:
    def __init__(self, db_path="vocabulary.db"):
        self.db_path = db_path
    
    def execute(self, query, params=(), fetch=False):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall() if fetch else None
        return result
    
    