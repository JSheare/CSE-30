# author: Jacob Shearer
# date: 6/5/2023
# file: calculatorGUI.py is a script that creates a calculator GUI. Users can use the GUI like a normal calculator
# input: button presses
# output: answers to mathematical expressions in the form of floating point/integer numbers

from tkinter import *
from calculator import calculate


def calculator(gui):
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=
    b0 = addButton(gui, entrybox, '0')
    b1 = addButton(gui, entrybox, '1')
    b2 = addButton(gui, entrybox, '2')
    b3 = addButton(gui, entrybox, '3')
    b4 = addButton(gui, entrybox, '4')
    b5 = addButton(gui, entrybox, '5')
    b6 = addButton(gui, entrybox, '6')
    b7 = addButton(gui, entrybox, '7')
    b8 = addButton(gui, entrybox, '8')
    b9 = addButton(gui, entrybox, '9')
    b_add = addButton(gui, entrybox, '+')
    b_sub = addButton(gui, entrybox, '-')
    b_mult = addButton(gui, entrybox, '*')
    b_div = addButton(gui, entrybox, '/')
    b_clr = addButton(gui, entrybox, 'c')
    b_dec = addButton(gui, entrybox, '.')
    b_exp = addButton(gui, entrybox, '^')
    b_op = addButton(gui, entrybox, '(')
    b_cp = addButton(gui, entrybox, ')')
    b_eq = addButton(gui, entrybox, '=')

    # add buttons to the grid
    buttons = [b7, b8, b9, b_clr,
               b4, b5, b6, b_mult,
               b1, b2, b3, b_div,
               b_exp, b0, b_sub, b_add,
               b_dec, b_op, b_cp, b_eq]
    k = 4
    for i in range(k+1):
        for j in range(k):
            buttons[i * k + j].grid(row=i + 1, column=j, columnspan=1)


def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command=lambda: clickButton(entrybox, value))


def clickButton(entrybox, value):
    global input_allowed
    # Evaluates the expression if an equals sign is entered and adds the answer to the entrybox
    if value == '=':
        expression = entrybox.get()
        entrybox.insert('end', ' = ')
        try:
            answer = calculate(expression)
            # If the answer is an integer then add it to the entry box as such
            if int(answer) == answer:
                entrybox.insert('end', str(int(answer)))
            else:
                entrybox.insert('end', answer)

            input_allowed = False
        except SyntaxError:
            entrybox.insert('end', 'Error')
            input_allowed = False

    # Clears the entrybox if c is entered
    elif value == 'c':
        entrybox.delete(0, END)
        input_allowed = True
    # All other button presses
    else:
        if input_allowed:
            entrybox.insert('end', value)


# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# Prevent input without clearing expression first
input_allowed = True
# update the window
gui.mainloop()

