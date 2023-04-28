

def sum_list(list):
    list_len = len(list)
    if list_len <= 1:
        if list_len == 1:
            return list[0]
    else:
        return list[0] + sum_list(list[1:])


if __name__ == '__main__':
    listA = []
    listB = [3]
    listC = [1, 2, 3, 4]
    assert sum_list(listA) == None
    assert sum_list(listB) == 3
    assert sum_list(listC) == 10
    print('Everything works correctly!')
