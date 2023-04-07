# author: Jacob Shearer
# date: 4/7/2023
# file: test_hangman.py tests a hangman.py
# input: file 'dictionary_short.txt'
# output: possible assertion errors

import hangman
import sys
import io

dictionary_file = 'dictionary_short.txt'

if __name__ == '__main__':
    # test import_dictionary(filename)
    dict_standard = {2: ['ad'],
                     3: ['bat'],
                     4: ['card'],
                     5: ['dress'],
                     6: ['engine'],
                     7: ['T-shirt'],
                     8: ['gasoline'],
                     9: ['gathering'],
                     10: ['evaluation'],
                     11: ['self-esteem'],
                     12: ['unemployment']}
    dictionary = hangman.import_dictionary(dictionary_file)
    assert dictionary == dict_standard

    # test get_game_options()
    output_standard = 'The word size is set to 4.\nYou have 4 lives.\n'
    hangman.input = lambda x: '4'  # redirect input
    stdout = sys.stdout
    sys.stdout = io.StringIO()  # redirect stdout
    size, lives = hangman.get_game_options()
    output = sys.stdout.getvalue()
    sys.stdout = stdout  # restore stdout
    assert size == 4
    assert lives == 4
    assert output == output_standard

    # test print_dicitonary()
    half1 = "2: ['ad']\n3: ['bat']\n4: ['card']\n5: ['dress']\n6: ['engine']\n7: ['T-shirt']\n"
    half2 = "8: ['gasoline']\n9: ['gathering']\n10: ['evaluation']\n11: ['self-esteem']\n12: ['unemployment']\n"
    dict_output_standard = half1 + half2
    sys.stdout = io.StringIO()  # redirect stdout
    hangman.print_dictionary(dictionary)
    dict_output = sys.stdout.getvalue()
    sys.stdout = stdout  # restore stdout
    assert dict_output == dict_output_standard

    # test print_display()
    letters_chosen = []
    display_list = ['__  ']*3
    lives = 2
    original_lives = 2
    display_standard = f'Letters chosen: \n__  __  __   lives: 2 OO\n'
    sys.stdout = io.StringIO()  # redirect stdout
    hangman.print_display(letters_chosen, display_list, lives, original_lives)
    display_output = sys.stdout.getvalue()
    sys.stdout = stdout  # restore stdout
    assert display_output == display_standard

    print('Everything looks good! No assertion errors!')
