def linear1(lst, value):
    """
    Retuns index of value from lst
    """
    i = 0
    while (i != len(lst) and lst[i] != value):
        i += 1
    if i != len(lst):
        return -1
    else:
        return i



def linear2(lst, value):
    """
    Retuns index of value from lst
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def linear3(lst, value):
    """
    Retuns index of value from lst
    """
    lst.append(value)
    i = 0
    while lst[i] != value:
        i += 1
    lst.pop()
    if i == len(lst):
        return -1
    else:
        return i

import timeit
file = open('linear_search.txt', 'w', encoding='utf-8')
print('while-loop function', file=file)
print(timeit.Timer(lambda: linear1(list(range(1000)), 0)).timeit(number=1), file=file)
print(timeit.Timer(lambda: linear1(list(range(1000)), 500)).timeit(number=1), file=file)
print(timeit.Timer(lambda: linear1(list(range(1000)), 1000)).timeit(number=1), file=file)
print('\nfor-loop function', file=file)
print(timeit.Timer(lambda: linear2(list(range(1000)), 0)).timeit(number=1), file=file)
print(timeit.Timer(lambda: linear2(list(range(1000)), 500)).timeit(number=1), file=file)
print(timeit.Timer(lambda: linear2(list(range(1000)), 1000)).timeit(number=1), file=file)
print('\nfunction with append and pop', file=file)
print(timeit.Timer(lambda: linear3(list(range(1000)), 0)).timeit(number=1), file=file)
print(timeit.Timer(lambda: linear3(list(range(1000)), 500)).timeit(number=1), file=file)
print(timeit.Timer(lambda: linear3(list(range(1000)), 1000)).timeit(number=1), file=file)
file.close()