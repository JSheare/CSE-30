class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)
