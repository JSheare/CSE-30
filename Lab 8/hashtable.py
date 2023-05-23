class Hashtable:
    def __init__(self, size=8):
        self.size = size
        self.table = [[] for s in range(self.size)]

    def __len__(self):
        n_items = 0
        for inner_list in self.table:
            for item in inner_list:
                n_items += 1

        return n_items

    def __hash(self, key):
        h_sum = 0
        for pos in range(len(key)):
            h_sum += ord(key[pos])

        return h_sum % self.size

    def get(self, key):
        index = self.__hash(key)
        inner_list = self.table[index]
        for item in inner_list:
            if item[0] == key:
                return item[1]

        return None

    def get_size(self):
        return self.size

    def add(self, key, value):
        index = self.__hash(key)
        inner_list = self.table[index]
        already_inside = False
        for item in inner_list:
            if item[0] == key:
                item[1] = value
                already_inside = True
                break

        if not already_inside:
            inner_list.append((key, value))

    def remove(self, key):
        index = self.__hash(key)
        inner_list = self.table[index]
        desired_item = None
        for item in inner_list:
            if item[0] == key:
                desired_item = item
                break

        if desired_item is not None:
            inner_list.remove(desired_item)

    def is_empty(self):
        return True if self.__len__() == 0 else False


if __name__ == '__main__':

    data = ['goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', 'cow', 'cat']

    # make a hash table with key-value pairs: 'goat': 0, 'pig': 1, 'chicken': 2, etc.
    h = Hashtable()
    for i in range(len(data)):
        h.add(data[i], i)  # the key is data[i], the value is i

    # print the hash table items
    for key in data:
        print(h.get(key))

    # test the method get() and if items in the hash table are correct
    for i in range(len(data)):
        assert h.get(data[i]) == i

        # test the method get_size()
    n = h.get_size()  # returns the size of the hash table array
    assert n == 8
    print(h.table)
    assert len(h) == 8  # returns the number of items in the hash table

    # test the method remove() and is_empty()
    for i in data:
        h.remove(i)
    print(h.is_empty())
    assert h.is_empty()
    assert len(h) == 0
    assert h.get_size() == 8
