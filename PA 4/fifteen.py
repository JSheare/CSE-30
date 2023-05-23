# author: Jacob Shearer
# date:
# file:
# input:
# output:

import numpy as np
from random import choice
from graph import Graph


class Fifteen:
    def __init__(self, size=4):
        self.size = size
        self.empty_tile_vertex = None
        # Makes the graph and adds all the tile vertices
        self.game_graph = Graph()
        for i in range(1, self.size**2 + 1):
            self.game_graph.addVertex(i)
            vertex = self.game_graph.getVertex(i)
            if i == self.size**2:
                vertex.value = 0
                self.empty_tile_vertex = vertex
            else:
                vertex.value = i

        # Connects all the vertices with their allowed edges
        corner_list = [1, self.size, self.size*(self.size-1) + 1, self.size**2]
        top_list = [s for s in range(2, self.size)]
        bottom_list = [s for s in range(self.size**2 - (self.size-2), self.size**2)]
        left_list = [s for s in range(1+self.size, self.size*(self.size-1), self.size)]
        right_list = [s for s in range(2*self.size, self.size**2, self.size)]
        for i in range(1, self.size**2 + 1):
            if i in corner_list:  # Corners
                one_factor = (-1)**((i % self.size) + 1)
                size_factor = -1 * self.size if i//self.size > 1 else self.size
                self.game_graph.addEdge(i, i+one_factor)
                self.game_graph.addEdge(i, i+size_factor)
            elif i in top_list or i in bottom_list:  # Top and bottom non-corner tiles
                size_factor = -1 * self.size if i in bottom_list else self.size
                self.game_graph.addEdge(i, i-1)
                self.game_graph.addEdge(i, i+1)
                self.game_graph.addEdge(i, i+size_factor)
            elif i in left_list or i in right_list:  # Left and right non-corner tiles
                one_factor = -1 if i in right_list else 1
                self.game_graph.addEdge(i, i-self.size)
                self.game_graph.addEdge(i, i+self.size)
                self.game_graph.addEdge(i, i+one_factor)
            else:  # Central tiles
                self.game_graph.addEdge(i, i-self.size)
                self.game_graph.addEdge(i, i+self.size)
                self.game_graph.addEdge(i, i-1)
                self.game_graph.addEdge(i, i+1)

    # Returns a string representation of the graph of tiles as a 2d array
    def __str__(self):
        s = ''
        for i in range(1, self.size**2 + 1):
            vertex = self.game_graph.getVertex(i)
            if vertex.value == 0:
                s += '   '
            elif vertex.value//10 >= 1:
                s += f'{vertex.value} '
            else:
                s += f' {vertex.value} '

            if i % self.size == 0:
                s += '\n'

        return s

    # Updates the values of the tiles
    def update(self, move):
        if self.is_valid_move(move):
            connections = list(self.empty_tile_vertex.getConnections())
            for connection in connections:
                if connection.value == move:
                    self.transpose(self.empty_tile_vertex, connection)
                    break

    # exchange i-tile with j-tile
    def transpose(self, i, j):
        i.value, j.value = j.value, i.value
        self.empty_tile_vertex = j

    # shuffle tiles
    def shuffle(self, steps=100):
        # Resets board to solved state first
        for i in range(1, self.size**2 + 1):
            vertex = self.game_graph.getVertex(i)
            if i == self.size ** 2:
                vertex.value = 0
                self.empty_tile_vertex = vertex
            else:
                vertex.value = i

        # Shuffles the board by doing steps random allowed moves
        for i in range(steps):
            connections = list(self.empty_tile_vertex.getConnections())
            move_vertex = choice(connections)
            self.transpose(self.empty_tile_vertex, move_vertex)

    # Checks if a move is valid: one of the tiles is 0 and another tile is its neighbor
    def is_valid_move(self, move):
        connections = list(self.empty_tile_vertex.getConnections())
        for connection in connections:
            if connection.value == move:
                return True

        return False

    # Verifies if the puzzle is solved
    def is_solved(self):
        for i in range(1, self.size**2):
            vertex = self.game_graph.getVertex(i)
            if vertex.value != i:
                return False

        return True

    # Draws the layout with tiles:
    def draw(self):
        value_list = []
        for i in self.game_graph.getVertices():
            vertex = self.game_graph.getVertex(i)
            if vertex.value == 0:
                value_list.append('   ')
            else:
                if vertex.value//10 >= 1:
                    value_list.append(f'{vertex.value} ')
                else:
                    value_list.append(f' {vertex.value} ')

        print('+' + self.size*'---+')
        index = 0
        for i in range(self.size):
            s = '|'
            for j in range(self.size):
                s += f'{value_list[index]}|'
                index += 1

            print(s)
            print('+' + self.size*'---+')

    # verify if the puzzle is solvable
    def is_solvable(self):
        pass

    # solve the puzzle
    def solve(self):
        pass
    

if __name__ == '__main__':
    
    # game = Fifteen()
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_valid_move(15) is True
    # assert game.is_valid_move(12) is True
    # assert game.is_valid_move(14) is False
    # assert game.is_valid_move(1) is False
    # game.update(15)
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    # game.update(15)
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_solved() is True
    # game.shuffle()
    # assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_solved() is False

    # You should be able to play the game if you uncomment the code below
    game = Fifteen(4)
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

    
    
        
