from timeit import Timer, timeit
import random
from matplotlib import pyplot as plt


def analyze(fxn, data):
    times = []
    for d in data:
        t1 = Timer(f"{fxn}({d})", f"from __main__ import {fxn}")
        times.append(t1.timeit(number=5))

    return times


def bubbleSort(items):
    for i in range(len(items)-1, 0, -1):
        for j in range(i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    return items


def mergeSort(items):
    if len(items) > 1:
        mid = len(items)//2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                items[k] = l[i]
                i += 1
            else:
                items[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            items[k] = l[i]
            i, k = i+1, k+1
        while j < len(r):
            items[k] = r[j]
            j, k = j+1, k+1

    return items


if __name__ == '__main__':
    # generate lists of random numbers from 0 to 500
    d1 = random.sample(range(0, 500), 10)
    d2 = random.sample(range(0, 500), 20)
    d3 = random.sample(range(0, 500), 50)
    d4 = random.sample(range(0, 500), 100)
    d5 = random.sample(range(0, 500), 200)

    # use random lists as input
    data = [d1, d2, d3, d4, d5]
    time = analyze('bubbleSort', data)
    plt.plot([len(i) for i in data], time, 'r', label='bubbleSort')

    time = analyze('mergeSort', data)
    plt.plot([len(i) for i in data], time, 'b', label='mergeSort')
    plt.legend()
    plt.show()
