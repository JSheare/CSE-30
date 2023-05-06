# author: Jacob Shearer
# date: 5/5/2023
# file: stack.py implements the stack ADT
# input: objects of any type
# output: a Stack object


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return False if len(self.items) > 0 else True

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None

    def size(self):
        return len(self.items)


# a driver program for class Stack
if __name__ == '__main__':
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() is None
