# assignment: programming assignment 1
# author: Jacob Shearer
# date: 4/7/2023
# file: hangman.py is a program that plays the popular 'hangman' game. Users try to determine what a randomly-chosen
#   word is by guessing letters until either the word has been found or the number of lives is exhausted.
# input: A text file containing a variety of words; characters.
# output: No output. Game is printed in the terminal.

import random as random
from random import choice


# Make a dictionary from a dictionary file ('dictionary.txt', see above)
def import_dictionary(filename):
    dictionary = {}
    min_size = 2
    max_size = 12
    try:
        for i in range(min_size, max_size+1):
            dictionary.update({i: []})

        dict_file = open(filename, 'r')
        words = dict_file.read().split('\n')
        dict_file.close()
        for word in words:
            word = word.replace(' ', '')
            word_len = len(word)
            if min_size <= word_len <= max_size:
                dictionary[word_len].append(word)
            elif word_len > max_size:
                dictionary[max_size].append(word)

    except FileNotFoundError:
        print('Not a valid dictionary file.')

    return dictionary


# Print the dictionary (use only for debugging)
def print_dictionary(dictionary):
    min_size = 2
    max_size = 12
    for i in range(min_size, max_size+1):
        print(f'{i}: {dictionary[i]}')


# Get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    min_size = 3
    max_size = 12
    size = 0
    lives = 0

    # Get the size of the word from the user
    try:
        size = int(input('Please choose a size of a word to be guessed [3 - 12, default any size]:\n'))
        if size < min_size or size > max_size:
            raise ValueError

        print(f'The word size is set to {size}.')
    except ValueError:
        size = random.randint(min_size, max_size)
        print('A dictionary word of any size will be chosen.')

    try:
        lives = int(input('Please choose a number of lives [1 - 10, default 5]:\n'))
        if lives > 10 or lives < 1:
            raise ValueError

    except ValueError:
        lives = 5

    print(f'You have {lives} lives.')
    return size, lives


# Format and print the game interface:
def print_display(letters_chosen, display_list, lives, original_lives):
    letters_chosen_string = str(letters_chosen).replace("'", '').replace('[', '').replace(']', '')
    display_string = ''
    for character in display_list:
        display_string += character

    lives_string = 'X' * (original_lives - lives) + 'O' * lives

    print(f'Letters chosen: {letters_chosen_string}')
    print(f'{display_string} lives: {lives} {lives_string}')


# MAIN
if __name__ == '__main__':
    dictionary_file = 'dictionary.txt'
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    # print_dictionary(dictionary)

    # print a game introduction
    print('Welcome to the Hangman Game!')

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while True:
        # Set up game options (the word size and number of lives)
        size, lives = get_game_options()

        # Select a word from a dictionary (according to the game options)
        valid_words = dictionary[size]
        word = ''
        if len(valid_words) > 1:
            word = choice(valid_words).upper()
        else:
            word = valid_words[0].upper()

        original_lives = lives
        letters_chosen = []
        word_list = [*word]
        display_list = ['__  ']*size
        current_state = ['_']*size
        for i in range(len(word_list)):
            if word_list[i] == '-':
                display_list[i] = '-  '
                current_state[i] = '-'

        # START GAME LOOP   (INNER PROGRAM LOOP)
        while True:
            # format and print the game interface:
            print_display(letters_chosen, display_list, lives, original_lives)

            # ask the user to guess a letter
            while True:
                guess = input('Please choose a new letter >\n').upper()
                if guess in letters_chosen:
                    print('You have already chosen this letter.')
                elif len(guess) > 1 or not guess.isalpha():
                    continue
                else:
                    break

            # update the list of chosen letters
            letters_chosen.append(guess)

            # if the letter is correct update the hidden word,
            if guess in word_list:
                print('You guessed right!')
                for i in range(len(word_list)):
                    if word_list[i] == guess:
                        display_list[i] = f'{guess}  '
                        current_state[i] = guess

            # else update the number of lives
            else:
                print('You guessed wrong, you lost one life.')
                lives -= 1

            if current_state == word_list:
                print_display(letters_chosen, display_list, lives, original_lives)
                print(f'Congratulations!!! You won! The word is {word}!')
                break
            elif lives == 0:
                print_display(letters_chosen, display_list, lives, original_lives)
                print(f'You lost! The word is {word}!')
                break

            # END GAME LOOP   (INNER PROGRAM LOOP)

        # ask if the user wants to continue playing,
        # if yes start a new game, otherwise terminate the program
        again = input('Would you like to play again [Y/N]?\n')
        if again in ['y', 'Y']:
            continue
        else:
            print('Goodbye!')
            break

    # END MAIN LOOP (OUTER PROGRAM LOOP)
