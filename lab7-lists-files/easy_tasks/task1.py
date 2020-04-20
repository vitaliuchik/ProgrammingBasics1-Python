def sieve_flavius(sup):
    """
    (int) -> list

    Return list of lucky numbers from 1 to sup
    Precondition: sup > 0

    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    """
    lst = []
    lst.append([i + 1 for i in range(sup)])

    lst.append([])
    for i in range(len(lst[0])):
        if (i + 1) % 2 != 0:
            lst[1].append(lst[0][i])
    count = 1
    while(count < len(lst[count]) - 1):
        lst.append([])
        for i in range(len(lst[count])):
            if (i + 1) % lst[count][count] != 0:
                lst[count + 1].append(lst[count][i])
        count += 1
    return lst[-1]


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
