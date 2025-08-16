import argparse
import sqlite3
from utils.DBManager import DBManager
from objects.adder import add_word as adder_add_word
from utils.Context import Context

def add_deck(name, context):
    db = DBManager()
    db.execute("INSERT INTO decks (name, parent_id) VALUES (?, ?)", (name, context.current_deck_id))
    print(f"Deck '{name}' added under deck ID {context.current_deck_id or 'root'}") # Review
    
def move_to_deck(name, context):
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
        

def add_word(word, context):
    adder_add_word(word, context)

# Lists the contents of the current deck, which consists of words and sub decks.
def list_current_deck(context: Context):
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

def run_interactive():
    from utils.Context import Context
    context = Context()
    print("Entering interactive mode. Type 'exit' to quit.")
    while True:
        try:
            line = input(">>> ").strip()
            if line.lower() in {"exit", "quit"}:
                break
            if not line:
                continue
            import shlex
            args = parse_args(shlex.split(line))
            print(args)
            handle_args(args, context)
            
        except Exception as e:
            print(f"Error: {e}")
       
       
# ---------- ARGPARSE SETUP ----------  
def parse_args(args_list=None):
    parser = argparse.ArgumentParser(description="Vocabulary CLI App")
    subparsers = parser.add_subparsers(dest="command")
    
    
    # ---- ADD Commands ----
    
    # We will have 'add deck' and 'add word'
    add_parser = subparsers.add_parser("add", help="Add decks or objects")
    add_subparsers = add_parser.add_subparsers(dest="add_command")
    
    
    add_deck = add_subparsers.add_parser("deck", help="Add a new deck")
    add_deck.add_argument("name", help="Name of the deck")
    
    add_obj = add_subparsers.add_parser("word", help="Add a new word")
    add_obj.add_argument("term", help="The word)")
    

    # ---- List Commands ----
    subparsers.add_parser("list")
    
    
    # --- Interactive Mode ----
    subparsers.add_parser("interactive")
    
    move_parser = subparsers.add_parser("move", help="Move into a subdeck")
    move_parser.add_argument("name")
    
    return parser.parse_args(args_list)
    

def handle_args(args, context=None):
    # 'context' can store the current deck ID if applicable
    if args.command == "add":
        if args.add_command == "deck":
            add_deck(args.name, context)
        elif args.add_command == "word":
            print("got here")
            add_word(args.term, context)
        else:
            print("You must specify to add either a deck or word")
    elif args.command == "list":
        list_current_deck(context)
    elif args.command == "move":
        move_to_deck(args.name, context)
    else:
        print("Unknown command.")
    

def main():
    args = parse_args()
    if args.command == "interactive":
        run_interactive()
    else:
        handle_args(args)
        

if __name__ == "__main__":
    main()
    
    