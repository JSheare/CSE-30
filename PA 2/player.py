# author:
# date:
# file: player.py
# input:
# output:

from random import choice


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
        # Prompts the user to choose a cell
        # If the user enters a valid string and the cell on the board is empty, updates the board
        # Otherwise prints a message that the input is wrong and rewrites the prompt
        cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n')
        # Cell must contain 2 characters
        condition_1 = True if len(cell) == 2 else False
        if condition_1:
            # Cell must contain one letter and one number in the first and second positions respectively
            condition_2 = True if cell[0].isalpha() and cell[1].isnumeric() else False
            # The cell letter must be either 'A', 'B', or 'C' and the number must be '1', '2', or '3'
            condition_3 = True if cell[0].upper() in ['A', 'B', 'C'] and cell[1] in ['1', '2', '3'] else False
        else:
            condition_2 = False
            condition_3 = False

        if condition_1 and condition_2 and condition_3:  # Valid cell choice
            if board.isempty(cell.upper()):  # Recursion base condition
                board.set(cell.upper(), self.sign)
            else:
                print('You did not choose correctly.\n')
                self.choose(board)

        else:
            print('You did not choose correctly.\n')
            self.choose(board)


class AI(Player):
    def __init__(self, name, sign, board):
        super().__init__(name, sign)
        self.board = board
        self.board_cells = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

    def choose(self, board):
        cell = choice(self.board_cells)
        if board.isempty(cell):  # Recursion base condition
            board.set(cell, self.sign)
        else:
            self.choose(board)


class MiniMax(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)
        self.opponent_sign = 'X' if self.sign == 'O' else 'O'

    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)

    def minimax(self, board, self_player, start):
        # Checks the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == '':
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1

        else:
            max_score = float('-inf')
            min_score = float('inf')
            move = ''
            # Makes a move (chooses a cell) recursively
            for cell in self.board_cells:
                # First checks to see if the chosen cell is empty
                if board.isempty(cell):
                    if self_player:
                        board.set(cell, self.sign)
                        score = self.minimax(board, False, False)
                        # If the new score is more than max_score than this is the best move found (so far)
                        if score > max_score:
                            max_score = score
                            move = cell

                    else:
                        board.set(cell, self.opponent_sign)
                        score = self.minimax(board, True, False)
                        # If the new score is less than min_score than this is the best move found (so far)
                        if score < min_score:
                            min_score = score
                            move = cell

                    # Undoing the test moves each time
                    board.set(cell, ' ')
                    board.winner = ''

                else:  # occupied cells are skipped
                    continue

            if start:  # Top of the recursion tree
                return move
            elif self_player:
                return max_score
            else:
                return min_score


class SmartAI(AI):
    def choose(self, board):
        print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ')
        move_cell = ''
        # Checks to see how many cells are occupied
        num_cells_occupied = 0
        cells_occupied = []
        for cell in self.board_cells:
            if board.isempty(cell):
                num_cells_occupied += 1
                cells_occupied.append(cell)

        # Starts on the corners OR in the middle (depending on availability) if only one cell is occupied
        if num_cells_occupied >= 8:
            for cell in ['B2', 'A1', 'C1', 'A3', 'C3']:
                if board.isempty(cell):
                    move_cell = cell
                    break

        # For non-starter moves
        else:
            def value_to_key(dict, val):  # converts indices to cell names
                keys = [k for k, v in dict.items() if v == val]
                if keys:
                    return keys[0]

            combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            opponent_sign = 'X' if self.sign == 'O' else 'O'
            # Prevent opponent from winning (this is given first priority)
            for combo in combos:
                symbols = [board.board[combo[0]], board.board[combo[1]], board.board[combo[2]]]
                if symbols.count(opponent_sign) == 2 and symbols.count(' ') == 1:
                    move_cell = value_to_key(board.board_dict, combo[symbols.index(' ')])
                    break

            # Finish out winning combinations (this is given second priority)
            if move_cell == '':
                for combo in combos:
                    symbols = [board.board[combo[0]], board.board[combo[1]], board.board[combo[2]]]
                    if symbols.count(self.sign) == 2 and symbols.count(' ') == 1:
                        move_cell = value_to_key(board.board_dict, combo[symbols.index(' ')])
                        break

            # Ordinary move
            if move_cell == '':
                for combo in combos:
                    symbols = [board.board[combo[0]], board.board[combo[1]], board.board[combo[2]]]
                    if ' ' in symbols:
                        move_cell = value_to_key(board.board_dict, combo[symbols.index(' ')])
                        break

        print(move_cell)
        board.set(move_cell, self.sign)
