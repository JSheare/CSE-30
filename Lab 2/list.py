def list_comprehension(old_list):
    # Returns a list containing sums of consecutive terms in the input list
    return [x + y for x, y in zip(old_list, old_list[1:])]


if __name__ == '__main__':
    A = [1, 3, 2, 4]
    # A = [1]
    print(A)
    print(list_comprehension(A))
