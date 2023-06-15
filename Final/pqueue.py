class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class PriorityQueue:
    def __init__(self):
        self.queue = Queue()

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return self.queue.isEmpty()

    def add(self, item):
        self.queue.enqueue(item)
        queue = self.queue.items
        for i in range(len(queue) - 1, 0, -1):
            for j in range(i):
                if queue[j] > queue[j+1]:
                    queue[j], queue[j+1] = queue[j+1], queue[j]

    def remove(self):
        returnval = self.queue.dequeue()
        queue = self.queue.items
        for i in range(len(queue) - 1, 0, -1):
            for j in range(i):
                if queue[j] > queue[j+1]:
                    queue[j], queue[j+1] = queue[j+1], queue[j]

        return returnval


if __name__ == '__main__':
    pq = PriorityQueue()
    data = [1, 3, 5, 2, 0, 6, 4]
    for i in data:
        print('adding', i)
        pq.add(i)
        print(pq)

    while not pq.empty():
        print('removing', pq.remove())
        print(pq)