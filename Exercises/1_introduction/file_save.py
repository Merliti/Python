"""
    Create an empty text file.
    Write a program that takes a list of words from the user and saves them in a file.
"""
import os


def words_to_file():
    with open("words.txt", "a") as f:

        print("Lets save some words to a file. Write 'exit' to save file")
        i = True
        while i:
            word = input("Write the word to add: ")
            word.lower()
            if word == 'exit':
                i = False
            else:
                f.write(f"{word}\n")

    f.close()

words_to_file()