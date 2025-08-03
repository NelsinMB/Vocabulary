import argparse
import sqlite3
from utils.DBManager import DBManager
from objects.adder import add_word

def main():
    db = DBManager()

    parser = argparse.ArgumentParser(description="Vocabulary CLI App")
    subparsers = parser.add_subparsers(dest="command") # dest="command" saves the subcommand name in args.command
    
    add_parser = subparsers.add_parser("add", help="Add a new word") # this will probably change to a more general add object
    add_parser.add_argument("word") #args.word will be the argument supplied
    

    subparsers.add_parser("list-words", help ="List all words")
    
    subparsers.add_parser("interactive", help="Start interactive mode")
    
    deck_parser = subparsers.add_parser("deck", help="Deck related commands")
    deck_sub = deck_parser.add_subparsers(dest="deck_command")
    
    deck_create = deck_sub.add_parser("create", help="Create a new deck")
    deck_create.add_argument("name")
    
    deck_sub.add_parser("list") # List all of the decks
    
    deck_add = deck_sub.add_parser("add_word")
    deck_add.add_argument("word")
    
    
    args = parser.parse_args()
    

    if args.command == 'list-words':
        result = db.execute("SELECT * FROM vocab", (), True)
        print(result)
    
    if args.command == 'add':
        add_word(args.word)
        
    if args.command == "interactive":
        run_interactive()


def run_interactive():
    print("Entering interactive mode. Type 'exit' to quit.")
    while True:
        try:
            command = input(">>> ").strip()
            if command.lower() in {"exit", "quit"}:
                break
            elif not command:
                continue
            else:
                import shlex
                args = shlex.split(command)
                main_from_args(args)
        except Exception as e:
            print(f"Error: {e}")
            
def main_from_args(args_list):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("word")

    subparsers.add_parser("list-words")

    args = parser.parse_args(args_list)

    if args.command == "add":
        print(f"Adding word: {args.word}")
    elif args.command == "list-words":
        print("Listing words...")
    else:
        parser.print_help()

        

if __name__ == "__main__":
    main()
    
    