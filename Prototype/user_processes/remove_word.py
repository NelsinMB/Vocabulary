from utils.DBManager import DBManager
from utils.Context import Context

# Need to delete first from deck_words.
# Check if the word belongs to any deck at all, if yes, leave it in words table. Otherwise, remove it from words.
# For the term, 

def remove_word(term, context: Context):
    deck_id = context.current_deck_id
    
    db = DBManager()
    word_id = db.execute("SELECT id FROM words WHERE term = ?", (term, ),
                         fetch=True)[0][0]
    
    db.execute("DELETE FROM deck_words WHERE deck_id = ? AND word_id = ?", (deck_id, word_id ) )
    print(f"Word '{term}' removed from deck ID {context.current_deck_id or 'root'}") # Review
    
    
    
    
    

    