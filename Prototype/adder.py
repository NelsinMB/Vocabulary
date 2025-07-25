import sqlite3

def add_word(word):
    con = sqlite3.connect("vocabulary.db")
    cur = con.cursor() # What is a cursor?

    cur.execute("CREATE TABLE IF NOT EXISTS vocab(word, definition)")
    #res = cur.execute("SELECT name FROM sqlite_master") # What does this do?
    #res.fetchone() # What does this do?

    cur.execute("""INSERT INTO vocab VALUES (?, 'test definition') """, (word,))
    con.commit()

def find_definition(word):
    pass

