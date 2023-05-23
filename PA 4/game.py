# author: Jacob Shearer
# date:
# file:
# input:
# output:

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
          

def clickButton(button_value):
    global input_allowed
    global moves
    move = tiles.game_graph.getVertex(int(button_value)).value
    if tiles.is_valid_move(move) and input_allowed:
        moves += 1
        gui.nametowidget('move_counter').configure(text=f'Moves: {moves}')
        # Updates the tiles
        old_blank = str(tiles.empty_tile_vertex.id)
        tiles.update(move)
        new_blank = str(tiles.empty_tile_vertex.id)
        # Updates the buttons
        gui.nametowidget(old_blank).configure(bg='orange', text=str(move))
        gui.nametowidget(new_blank).configure(bg='white', text='')

        # Turns all tiles blue once the puzzle has been solved
        if tiles.is_solved():
            for i in range(1, size**2 + 1):
                gui.nametowidget(str(i)).configure(bg='blue')

            # Disables input without reshuffling
            input_allowed = False


def shuffle():
    global input_allowed
    global moves
    # Shuffles the tiles
    tiles.shuffle()
    # Updates the buttons to reflect the new tile ordering
    for i in range(1, size**2 + 1):
        vertex = tiles.game_graph.getVertex(i)
        label = '' if vertex.value == 0 else str(vertex.value)
        color = 'white' if vertex.value == 0 else 'orange'
        gui.nametowidget(str(i)).configure(bg=color, text=label)

    # Resets the moves counter
    moves = 0
    gui.nametowidget('move_counter').configure(text=f'Moves: {moves}')
    # Re-enables input
    input_allowed = True


if __name__ == '__main__':
    # Makes the tiles
    size = 4  # Yes this is adjustable. You could play a 10x10 puzzle if you really wanted to
    tiles = Fifteen(size)
    tiles.shuffle()

    # Makes the window
    gui = Tk()
    gui.title("Fifteen")

    # Sets the font
    font = font.Font(family='Helveca', size=25, weight='bold')

    # Making/adding buttons to the GUI
    for i in range(1, size**2 + 1):
        vertex = tiles.game_graph.getVertex(i)
        name = str(vertex.id)
        button_text = '' if vertex.value == 0 else str(vertex.value)
        button = Button(gui, text=button_text, name=name, bg='orange', fg='black', font=font, height=2, width=5,
                        command=lambda name=name: clickButton(name))

        if vertex.value == 0:
            button.configure(bg='white')

        # Adding the button to the window
        button.grid(row=(i-1)//size, column=(i-1) % size, columnspan=1)

    # Adding the shuffle button to the GUI
    shuffle_button = Button(gui, text='Shuffle', name='shuffle_button', bg='gray', fg='black', font=font,
                            height=1, width=8, command=lambda: shuffle())
    shuffle_button_width = 2 if size % 2 == 0 else 3
    shuffle_button.grid(row=size+1, column=int(size/2)-1, columnspan=shuffle_button_width)

    # Adds a move counter under the shuffle button
    moves = 0
    move_counter = Label(gui, fg='black', height=1, width=10, font=font, text=f'Moves: {moves}',
                         name='move_counter')
    move_counter.grid(row=size+2, column=int(size/2)-1, columnspan=shuffle_button_width)

    # Makes it so that the board can't be interacted with once solved (unless reshuffled)
    input_allowed = True

    # Updates the window
    gui.mainloop()
