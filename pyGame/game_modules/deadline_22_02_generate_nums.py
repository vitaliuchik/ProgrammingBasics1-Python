def ulam(sup):
    """
    (int) -> list

    Return list of Ulam's numbers from 1 to sup
    Precondition: sup > 1

    >>> ulam(16)
    [1, 2, 3, 4, 6, 8, 11, 13, 16]
    >>> ulam(1)
    [1]
    >>> ulam(2)
    [1, 2]
    """

    lst = [1, 2]
    number = lst[-1] + 1
    if sup == 1:
        return [1]
    while number <= sup:
        sum_count = 0
        for i in lst:
            if number - i in lst and number - i != i:
                sum_count += 1
        if sum_count == 2:
            lst.append(number)
        number += 1
    return lst

def lucky(sup):
    """
    (int) -> list

    Return list of lucky numbers from 1 to sup
    Precondition: sup > 0

    >>> lucky(16)
    [1, 3, 7, 9, 13, 15]
    >>> lucky(1)
    [1]
    """
    lst1 = [i + 1 for i in range(sup)]
    lst2 = []
    lst3 = []
    lst4 = []
    for i in range(len(lst1)):
        if (i + 1) % 2 != 0:
            lst2.append(lst1[i])
    for i in range(len(lst2)):
        if (i + 1) % 3 != 0:
            lst3.append(lst2[i])
    for i in range(len(lst3)):
        if (i + 1) % 7 != 0:
            lst4.append(lst3[i])
    return lst4

def even(sup):
    """
    (int) -> list

    Return list of even numbers from 2 to sup
    Precondition: sup > 0

    >>> even(16)
    [2, 4, 6, 8, 10, 12, 14, 16]
    >>> even(1)
    []
    """
    return [i for i in range(1, sup + 1) if i % 2 == 0]
