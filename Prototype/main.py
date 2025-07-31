import argparse
import sqlite3
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", help="Adds a new word to the system.") # Optional arguments must start with '-' or '--' in argparse
    parser.add_argument("-w", "--words", help="Displays all the words in the system", action="store_true")
    parser.add_argument("-c", "--convert", action="store_true")
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