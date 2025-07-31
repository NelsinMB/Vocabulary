import argparse
import sqlite3
def main():
    parser = argparse.ArgumentParser(description="Vocabulary CLI App")
    subparsers = parser.add_subparsers(dest="command") # dest="command" saves the subcommand name in args.command
    
    add_parser = subparsers.add_parser("add", help="Add a new word") # this will probably change to a more general add object
    add_parser.add_argument("word") #args.word will be the argument supplied
    
    subparsers.add("list-words", help ="List all words")
    
    deck_parser = subparsers.add_parser("deck", help="Deck related commands")
    deck_sub = deck_parser.add_subparsers(dest="deck_command")
    
    deck_create = deck_sub.add_parser("create", help="Create a new deck")
    deck_create.add_argument("name")
    
    deck_sub.add_parser("list") # List all of the decks
    
    deck_add = deck_sub.add_parser("add_word")
    deck_add.add_argument("word")
    
    
    args = parser.parse_args()


    if args.add is not None:
        from adder import add_word
        word = args.add
        add_word(word)
    
    if args.words is not None:
        from Utils import see_words
        see_words()
    
    if args.convert is not None:
        from Utils import convert_to_objects
        for entry in convert_to_objects("vocab"):
            print(entry.term)
    
if __name__ == "__main__":
    main()