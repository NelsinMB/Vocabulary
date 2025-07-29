import sqlite3
from Word import Word
from typing import List

# This prints out the words in the database to the terminal
def see_words():
    conn = sqlite3.connect('vocabulary.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM vocab")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

    conn.close()
    
# This takes in a list of rows from the database and returns them as objects. More for a proof of concept.
def convert_to_objects(conn, table_name) -> List[Word]:
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    result = []
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            new_word = Word(row[0], row[1], row[2], row[3], row[4])
            result.append(new_word)
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
    
    return result
        
    
        