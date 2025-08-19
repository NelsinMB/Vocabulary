from utils.DBManager import DBManager

def add_deck(name, context):
    db = DBManager()
    db.execute("INSERT INTO decks (name, parent_id) VALUES (?, ?)", (name, context.current_deck_id))
    print(f"Deck '{name}' added under deck ID {context.current_deck_id or 'root'}") # Review