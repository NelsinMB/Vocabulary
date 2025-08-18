import sqlite3
import requests
import sys
from datetime import datetime
from utils.DBManager import DBManager
from utils.Context import Context

def add_word_procedure(word, context: Context):
    definition = find_definition(word)
    response = input("The definition retrieved is: " +  find_definition(word) + "\n Type y if you are content with this definition, n if you are not and supply your own definition.")
    
    if response=="n":
        definition = input("Enter the definition: ")
        add_word(word, context, definition)
        
    elif response=="y":
        add_word(word, context, definition)
    else:
        print("Incorrect response")
        return
    
# Any time adding a word is performed, it is through this function. This ensures words and deck_words are in unison.
def add_word(word, context, definition):
    db = DBManager()
    db.execute("CREATE TABLE IF NOT EXISTS words(id, term, def)")
    db.execute("""INSERT INTO words (term, def) VALUES (?, ?) """, (word, definition)) 
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


