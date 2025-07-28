import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", help="Adds a new word to the system.") # Optional arguments must start with '-' or '--' in argparse
args = parser.parse_args()
word = args.add
print(word)

if args.add is not None:
    from adder import add_word
    add_word(word)
    

