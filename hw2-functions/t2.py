def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('a', 'A')
    False
    >>> compare_char('d', 'ad')

    >>> compare_char('2', 2)

    """
    if isinstance(ch1, str) and isinstance(ch2, str):
        if ch1.isalpha() and ch2.isalpha() and len(ch1) == 1 and len(ch2) == 1:
            (ch1, ch2) = (ch1.lower(), ch2.lower())
            return ch2 < ch1
    return None



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
