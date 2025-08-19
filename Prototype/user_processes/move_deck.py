from utils.DBManager import DBManager

def move_deck(name, context):
    db = DBManager()
    
    if name == "parent":
        result = db.execute(
            "SELECT parent_id FROM decks WHERE id IS ?", 
            (context.current_deck_id, ), 
            fetch = True
        )
        parent_id = result[0][0]
        result2 = db.execute(
            "SELECT name FROM decks WHERE id IS ?",
            (parent_id, ),
            fetch = True
        )
        parent_name = result2[0][0]
        context.set_deck(parent_id, parent_name)
        print(f"Moved into deck: {parent_name}")
    else:
        result = db.execute(
        "SELECT id FROM decks WHERE name = ? AND parent_id IS ?", 
        (name, context.current_deck_id),
        fetch = True
        )
        if result:
            deck_id = result[0][0] 
            # Result returns as a list even though name+parent is unique (need to make that it is indeed unique)
            # Then, we want the first entry of that row since it is the id
            context.set_deck(deck_id, name)
            print(f"Moved into deck: {name}")
        else:
            print(f"Deck '{name}' not found under current deck.")