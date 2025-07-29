# Generates a Python object for a word in the database

from Prototype import Word


def create_word_object(word: dict) -> Word:
    word_object = Word(word[name], word[meanings], )