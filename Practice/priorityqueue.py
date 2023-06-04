class PriorityQueue:
    def __init__(self):
        self.heapList = [0]
        self.heapData = [None]
        self.currentSize = 0

    def percUp(self, i):
        # i // 2 is the index of the parent node
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
                self.heapData[i // 2], self.heapData[i] = self.heapData[i], self.heapData[i // 2]

            i = i // 2

    def insert(self, key, value):
        self.heapList.append(key)
        self.heapData.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
                self.heapData[i], self.heapData[mc] = self.heapData[mc], self.heapData[i]

            i = mc

    def delMin(self):
        retval = self.heapData[1]
        # Setting the root of the heap to the last value of the heap
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapData[1] = self.heapData[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.heapData.pop()
        # Restoring heap order priority
        self.percDown(1)
        return retval

    def buildQueue(self, key_list, data_list):
        if len(key_list) != len(data_list):
            raise ValueError('ValueError: key_list and data_list must be the same length')

        i = len(key_list) // 2
        self.currentSize = len(key_list)
        self.heapList = [0] + key_list[:]
        self.heapData = [None] + data_list[:]
        while i > 0:
            self.percDown(i)
            i -= 1


if __name__ == '__main__':
    queue = PriorityQueue()
    queue.buildQueue([1, 5, 2, 3], ['lol', 'rofl', 'xd', 'lmfao'])
    queue.insert(4, 'epic')
    while queue.currentSize > 0:
        print(queue.delMin())
