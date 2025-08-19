from utils.DBManager import DBManager
from utils.Context import Context

# Lists the contents of the current deck, which consists of words and sub decks.
def list_deck(context: Context):
    db = DBManager()
    decks = db.execute(
        "SELECT name FROM decks WHERE parent_id IS ?", 
        (context.current_deck_id, ),
        fetch=True
    )
    decks = [entry[0] for entry in decks]
    words = db.execute(
        "SELECT w.term FROM words as w JOIN deck_words as dw ON w.id = dw.word_id WHERE dw.deck_id = ?",
        (context.current_deck_id, ),
        fetch=True
    )
    words = [entry[0] for entry in words]

    for deck in decks:
        print("Deck: ", deck)
    for word in words:
        print("Word: ",  word)