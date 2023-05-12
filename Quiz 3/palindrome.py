class Stack:
    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def is_palindrome(s):
    main_stack = Stack()
    temp_stack = Stack()
    for char in s:
        main_stack.push(char)

    search_letter = ''
    while True:
        letter = main_stack.pop()
        if search_letter == '':
            search_letter = letter
            continue
        else:
            if letter == search_letter:
                if temp_stack.size() <= 1:
                    return True
                else:
                    while not temp_stack.isEmpty():
                        main_stack.push(temp_stack.pop())

                search_letter = ''
            else:
                temp_stack.push(letter)
                if main_stack.size() == 0:
                    return False


if __name__ == '__main__':
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))
