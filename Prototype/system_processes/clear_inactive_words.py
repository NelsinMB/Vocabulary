from utils.DBManager import DBManager


def is_word_inactive(term: str) -> bool:
    """
    Checks whether a term belongs to no decks, returns true if so.
    
    Particularly useful for development/testing, when different tables of the database may become misaligned.
    
    Parameters:
    term: str
        The term to check the inactiveness of.
    
    """
    
    db = DBManager()
    word_id = db.execute("SELECT id FROM words WHERE term = ?", (term, ), fetch=True)
    
    if word_id == []:
        print("The word you searched for is not in the system.")
        return False 
    
    word_id = word_id[0][0] #return of SQL statement comes as [(X, )]
    
    
    # Find rows in deck_words where word_id is part of
    # If this is empty, then the term is not active. Otherwise, it is active.
    
    
    result = db.execute("SELECT deck_id, word_id FROM deck_words WHERE word_id = ?", (word_id, ), fetch=True)
    if result:
        return False
    else:
        return True
        
    
def clear_word_if_inactive(term):
    """
    Removes the a word from the 'words' table if it does not belong to any decks.
    
    Particularly useful for development/testing, when different tables of the database may become misaligned.
    
    Paramters:
    term: str
        The term to clear, if inactive.
    """
    
    db = DBManager()
    
    ''
    if is_word_inactive(term):
        db.execute("DELETE FROM words WHERE term = ?", (term, ))
        print("The term", term, "is  inactive in the system and has thus been purged from words.")
    else:
        print("The term", term, "is not inactive in the system.")
    
if __name__ == "__main__":
    import sys
    term = sys.argv[1]  # get the first argument from command line
    clear_word_if_inactive(term)