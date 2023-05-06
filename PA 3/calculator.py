# author: Jacob Shearer
# date: 5/5/2023
# file: calculator.py is a script that takes mathematical expressions in infix notation and evaluates them
# input: infix notation mathematical expressions in the form of strings
# output: answers to mathematical expressions in the form of floating point numbers

from stack import Stack
from tree import ExpTree


def infix_to_postfix(infix):
    # Initial infix string processing
    infix = infix.replace(' ', '')
    # The first character in the string should be either a digit, an opening parentheses, or a decimal point
    if not infix[0].isdigit() and infix[0] != '(' and infix[0] != '.':
        raise SyntaxError

    # The last character in the string should be either a digit, a closing parentheses, or a decimal point
    if not infix[-1].isdigit() and infix[-1] != ')' and infix[-1] != '.':
        raise SyntaxError

    previous_char = ''
    index = 0
    for char in infix:
        # Operators/decimal points should not occur to the right of opening parentheses
        if char in ['^', '*', '/', '+', '-', '.'] and previous_char == '(':
            raise SyntaxError

        # Operators should never be right next to one another
        if char in ['^', '*', '/', '+', '-'] and previous_char in ['^', '*', '/', '+', '-']:
            raise SyntaxError

        # Decimal points should never be right next to one another
        if char == '.' and previous_char == '.':
            raise SyntaxError

        # Decimal points should always have a digit to either the left or right
        if char == '.':
            next_is_digit = False
            try:
                next_char = infix[index+1]
                next_is_digit = True if next_char.isdigit() else False
            except IndexError:
                pass

            if not next_is_digit and not previous_char.isdigit():
                raise SyntaxError

        previous_char = char
        index += 1

    # Puts filtered infix string into the necessary format for .split() to work properly (i.e. space delimited)
    new_infix = ''
    for i in range(len(infix)):
        if i == len(infix) - 1:
            new_infix += infix[i]
        else:
            if infix[i].isdigit():
                # No spaces in the middle of floating point numbers
                if infix[i+1].isdigit() or infix[i+1] == '.':
                    new_infix += infix[i]
                else:
                    # Space after floating point/integer
                    new_infix += (infix[i] + ' ')

            # No spaces right after decimal points when in the middle of the floating point numbers
            elif infix[i] == '.':
                if infix[i+1].isdigit():
                    new_infix += '.'
                else:
                    new_infix += infix[i] + ' '

            else:
                new_infix += (infix[i] + ' ')

    infix_list = new_infix.split()
    # Simply typing nothing will raise an error
    if len(infix_list) == 0:
        raise SyntaxError
    if len(infix_list) == 1:
        # Just in case the user enters a single number
        try:
            float(infix_list[0])
            return infix_list[0]
        except ValueError:
            raise SyntaxError

    # Translating the infix expression into postfix
    else:
        operators = {'^': 5, '*': 4, '/': 3, '+': 2, '-': 1}
        opstack = Stack()
        postfix_list = []
        for token in infix_list:
            # Push open parentheses to stack
            if token == '(':
                opstack.push(token)
            # Start looking for open parentheses
            elif token == ')':
                opener = False
                while not opstack.isEmpty():
                    # All operators which aren't an open parentheses get added to the postfix list
                    item = opstack.pop()
                    if item == '(':
                        opener = True
                        break

                    postfix_list.append(item)

                # If no open parentheses is found raise a SyntaxError
                if not opener:
                    raise SyntaxError

            # Add operator to stack, but first add all operators of higher or equal precedence to postfix list
            elif token in operators:
                while True:
                    item = opstack.peek()
                    if opstack.isEmpty() or item == '(':
                        opstack.push(token)
                        break
                    elif operators[item] >= operators[token]:
                        postfix_list.append(opstack.pop())
                    else:
                        opstack.push(token)
                        break

            # All other operands are simply added to the postfix list
            else:
                postfix_list.append(token)

        # Add all remaining operators left in the stack to the postfix list
        while not opstack.isEmpty():
            postfix_list.append(opstack.pop())

        # Check for erroneous open parentheses, if found raise a SyntaxError
        if '(' in postfix_list:
            raise SyntaxError

        # If postfix is empty raise an error
        if len(postfix_list) == 0:
            raise SyntaxError

        return ' '.join(postfix_list)


def calculate(infix):
    postfix = infix_to_postfix(infix)
    # If the user only entered one number just return the number
    if len(postfix.split()) == 1:
        return float(postfix)
    # Otherwise, make a tree and traverse it
    else:
        tree = ExpTree.make_tree(postfix.split())
        return ExpTree.evaluate(tree)


if __name__ == '__main__':
    print('Welcome to Calculator Program!')
    while True:
        try:
            expression = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
            if expression.lower() in ['q', 'quit']:
                break

            answer = calculate(expression)
            print(answer)

        # Will run if the user enters something with a formatting issue
        except SyntaxError:
            print('Not a valid expression.')

    print('Goodbye!')

    # test infix_to_postfix function
    # assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    # assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # # test calculate function
    # assert calculate('(5+2)*3') == 21.0
    # assert calculate('5+2*3') == 11.0
