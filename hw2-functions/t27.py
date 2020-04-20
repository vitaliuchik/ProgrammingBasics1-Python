def turn_over(n, lst):
    """
    int, list(str) -> list(int)
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> turn_over(-5, [])
    []
    """
    if n <= 0:
        return []
    if n > len(lst):
        pass
    reversed = lst[:n]
    reversed = reversed[::-1]
    return reversed + lst[n:]


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
