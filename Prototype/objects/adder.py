import sqlite3
import requests
import sys
from datetime import datetime
from utils.DBManager import DBManager
from utils.Context import Context

def add_word(word, context: Context):
    db = DBManager()
    db.execute("CREATE TABLE IF NOT EXISTS words(id, term, def)")
    db.execute("""INSERT INTO words (term, def) VALUES (?, ?) """, (word, find_definition(word))) # Do i put a place holder for primary key?
    word_id = db.execute(
        "SELECT id FROM words WHERE term = ?",
                         (word, ), 
                         fetch=True
                         )[0][0]
    db.execute("INSERT INTO deck_words (deck_id, word_id) VALUES (?, ?)", 
                (context.current_deck_id, word_id)
    )

def find_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        definition = meanings[0]['definitions'][0]['definition']
        return definition
    else:
        return {}


