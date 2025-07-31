import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = sqlite3.connect("vocabulary.db")
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()
