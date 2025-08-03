import sqlite3
import requests
import sys
from datetime import datetime
from ..utils.DBManager import get_db_connection
from ..utils.DBManager import DBManager

def add_word(word):
    db = DBManager()
    db.execute("CREATE TABLE IF NOT EXISTS vocab(word, definition, creation_date, last_reviewed_date, review_count)")
    db.execute("""INSERT INTO vocab VALUES (?, ?, ?, ?, ?) """, (word, find_definition(word), datetime.now(), -1, 0))

def find_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        definition = meanings[0]['definitions'][0]['definition']
        return definition
    else:
        return {}


