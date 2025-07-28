import sqlite3
import requests

def add_word(word):
    con = sqlite3.connect("vocabulary.db")
    cur = con.cursor() # What is a cursor?

    cur.execute("CREATE TABLE IF NOT EXISTS vocab(word, definition)")
    #res = cur.execute("SELECT name FROM sqlite_master") # What does this do?
    #res.fetchone() # What does this do?

    #cur.execute("""INSERT INTO vocab VALUES (?, ?) """, (word, find_definition(word)))
    print(find_definition(word))
    con.commit()

def find_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        return {
            entry["partOfSpeech"]: [defn["definition"] for defn in entry["definitions"]]
            for entry in meanings
        }
    else:
        return {}


