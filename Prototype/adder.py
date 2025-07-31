import sqlite3
import requests
import sys
from datetime import datetime
from Utils.db_utils import get_db_connection

def add_word(word):
    with get_db_connection() as conn:
        cur = conn.cursor() 
        cur.execute("CREATE TABLE IF NOT EXISTS vocab(word, definition, creation_date, last_reviewed_date, review_count)")
        cur.execute("""INSERT INTO vocab VALUES (?, ?, ?, ?, ?) """, (word, find_definition(word), datetime.now(), -1, 0))

def find_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        definition = meanings[0]['definitions'][0]['definition']
        return definition
    else:
        return {}


