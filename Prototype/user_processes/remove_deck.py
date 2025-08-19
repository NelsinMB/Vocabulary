from utils.DBManager import DBManager

def remove_deck(name, context):
    db = DBManager()
    deck_id = context.current_deck_id
    
    db = DBManager()
    word_id = db.execute("SELECT id FROM words WHERE term = ?", (term, ),
                         fetch=True)[0][0]
    
    db.execute("DELETE FROM deck_words WHERE deck_id = ? AND word_id = ?", (deck_id, word_id ) )
    print(f"Word '{term}' removed from deck ID {context.current_deck_id or 'root'}") # Review