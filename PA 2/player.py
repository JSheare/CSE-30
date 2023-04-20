# author:
# date:
# file: player.py
# input:
# output:

from random import choice as choice


class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        # Returns an instance sign
        return self.sign

    def get_name(self):
        # Returns an instance name
        return self.name

    def choose(self, board):
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.isempty(cell), and board.set(cell, sign)
        cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n')
        condition_1 = True if len(cell) == 2 else False
        if condition_1:
            condition_2 = True if cell[0].isalpha() and cell[1].isnumeric() else False
            condition_3 = True if cell[0].upper() in ['A', 'B', 'C'] and cell[1] in ['1', '2', '3'] else False
        else:
            condition_2 = False
            condition_3 = False

        if condition_1 and condition_2 and condition_3:
            # Recursion base condition
            if board.isempty(cell):
                board.set(cell, self.sign)
            else:
                print('You did not choose correctly.\n')
                self.choose(board)

        else:
            print('You did not choose correctly.\n')
            self.choose(board)
