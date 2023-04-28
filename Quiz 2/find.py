

def find_max(list):
    if len(list) <= 1:
        if len(list) == 1:
            return list[0]
        else:
            return None
    else:
        result = find_max(list[1:])
        if result > list[0]:
            return result
        else:
            return list[0]


if __name__ == "__main__":
    listA = []
    listB = [3]
    listC = [1, 2, 3, 4]
    assert find_max(listA) == None
    assert find_max(listB) == 3
    assert find_max(listC) == 4
    print('Everything works correctly!')
