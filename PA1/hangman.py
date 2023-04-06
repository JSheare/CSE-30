# assignment: programming assignment 1
# author: Jacob Shearer
# date: 4/7/2023
# file: hangman.py is a program that (put the description of the program)
# input: (write input description)
# output: (write output description)

from random import choice, random

dictionary_file = "dictionary.txt"  # make a dictionary.txt in the same folder where hangman.py is located


# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary(filename):
    dictionary = {}
    max_size = 12
    try:
        pass
    except Exception:
        pass
    return dictionary


# print the dictionary (use only for debugging)
def print_dictionary(dictionary):
    max_size = 12
    pass


# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    pass
    return (size, lives)


# MAIN

if __name__ == '__main__':
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    print_dictionary(dictionary)  # remove after debugging the dictionary function import_dictionary

    # print a game introduction

    # START MAIN LOOP (OUTER PROGRAM LOOP)

    # set up game options (the word size and number of lives)

    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)

    # START GAME LOOP   (INNER PROGRAM LOOP)

    # format and print the game interface:
    # Letters chosen: E, S, P                list of chosen letters
    # __ P P __ E    lives: 4   XOOOO        hidden word and lives

    # ask the user to guess a letter

    # update the list of chosen letters

    # if the letter is correct update the hidden word,
    # else update the number of lives
    # and print interactive messages

    # END GAME LOOP   (INNER PROGRAM LOOP)

    # check if the user guesses the word correctly or lost all lives,
    # if yes finish the game

    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing,
    # if yes start a new game, otherwise terminate the program