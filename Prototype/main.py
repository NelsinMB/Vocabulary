import argparse
import sqlite3
from utils.DBManager import DBManager
from utils.Context import Context
from user_processes.add_word import add_word_procedure
from user_processes.add_deck import add_deck
from user_processes.move_deck import move_deck
from user_processes.list_deck import list_deck
from user_processes.remove_deck import remove_deck
from user_processes.remove_word import remove_word

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
    add_parser = subparsers.add_parser("add", help="Add decks or words")
    add_subparsers = add_parser.add_subparsers(dest="add_command")
    
    
    add_deck = add_subparsers.add_parser("deck", help="Add a new deck")
    add_deck.add_argument("name", help="Name of the deck")
    
    add_word = add_subparsers.add_parser("word", help="Add a new word")
    add_word.add_argument("term", help="The word")
    
    
    # ---- REMOVE Commands ----
    
    # We will have 'remove deck' and 'remove word'
    remove_parser = subparsers.add_parser("remove", help="Remove decks or words")
    remove_subparsers = remove_parser.add_subparsers(dest="remove_command")
    
    remove_deck = remove_subparsers.add_parser("deck", help="Remove an existing deck")
    remove_deck.add_argument("name", help="Name of the deck")
    
    remove_word = remove_subparsers.add_parser("word", help="Remove a new word")
    remove_word.add_argument("term", help="The word")
        
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
            add_word_procedure(args.term, context)
        else:
            print("You must specify to add either a deck or word")
    elif args.command == "remove":
        if args.remove_command == "deck":
            remove_deck(args.name, context)
        elif args.remove_command == "word":
            remove_word(args.term, context)
    elif args.command == "list":
        list_deck(context)
    elif args.command == "move":
        move_deck(args.name, context)
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
    
    