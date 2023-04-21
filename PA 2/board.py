# author: Jacob Shearer
# date: 4/20/2023
# file: board.py a python file containing the Board class used in tictac.py
# input: strings from the game
# output: bool values, strings, other game-related information, and the tic-tac-toe board itself


class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = ' '
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        self.board_dict = {'A1': 0, 'B1': 1, 'C1': 2, 'A2': 3, 'B2': 4, 'C2': 5, 'A3': 6, 'B3': 7, 'C3': 8}
        # the winner's sign O or X
        self.winner = ''

    def get_size(self):
        # Returns the board size (an instance size)
        return self.size**2

    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        return self.winner

    def set(self, cell, sign):
        # Converts A1, B1, …, C3 cells into index values from 0 to 8
        # Marks the cell on the board with the sign X or O
        cell_index = self.board_dict[cell]
        self.board[cell_index] = sign

    def isempty(self, cell):
        # Converts A1, B1, …, C3 cells into index values from 0 to 8
        # Returns True if the cell is empty (not marked with X or O)
        cell_index = self.board_dict[cell]
        return True if self.board[cell_index] == ' ' else False

    def isdone(self):
        done = False
        self.winner = ''
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X

        # Checks to see if the entire board has been filled
        occupied_cells = []
        for i in range(0, 9):
            if self.board[i] != ' ':
                occupied_cells.append(i)

        if occupied_cells == list(range(0, 9)):
            done = True

        # Checks to see if one of the winning combinations has been satisfied, and if so by who
        combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combo in combos:
            symbols = [self.board[combo[0]], self.board[combo[1]], self.board[combo[2]]]
            if ' ' in symbols:
                continue

            if symbols == ['X'] * 3:
                self.winner = 'X'
                done = True

            if symbols == ['O'] * 3:
                self.winner = 'O'
                done = True

        return done

    def show(self):
        # Draws the board
        print('\n   A   B   C  ')
        print(' +---+---+---+')
        print(f'1| {self.board[0]} | {self.board[1]} | {self.board[2]} |')
        print(' +---+---+---+')
        print(f'2| {self.board[3]} | {self.board[4]} | {self.board[5]} |')
        print(' +---+---+---+')
        print(f'3| {self.board[6]} | {self.board[7]} | {self.board[8]} |')
        print(' +---+---+---+\n')
