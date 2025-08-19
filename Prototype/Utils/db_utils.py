from Vocabulary.Prototype.utils.DBManager import DBManager
import sys

def wipe():
    db = DBManager()
    db.execute("DROP TABLE IF EXISTS words")
    db.execute("DROP TABLE IF EXISTS decks")
    db.execute("DROP TABLE IF EXISTS deck_words")
    print("All the tables in the database have been wiped.")

def clear_words():
    db = DBManager()
    db.execute("DELETE FROM words")
    db.execute("DELETE FROM deck_words") # If there are no words, there are no deck-word relations to preserve.
    print("The tables words and deck_words have been cleared.")
    
def clear_decks():
    db = DBManager()
    db.execute("DELETE FROM decks") 
    db.execute("DELETE FROM deck_words") # If there are no decks, there are no deck-word relations to preserve.
    print("The tables decks and deck_words have been cleared.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python db_utils.py [wipe | clear_words | clear_decks]")
        
    command = sys.argv[1]
    
    if command == "wipe":
        wipe()
    elif command == "clear_words":
        clear_words
    elif command == "clear_decks":
        clear_decks
    else:
        print("Command not recognized")
    