def get_position(ch):
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter function
    should return None.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    >>> get_position('12')

    >>> get_position('2a')

    >>> get_position(12)

    >>> get_position('')

    """
    if isinstance(ch, str):
        if ch.isalpha() and len(ch) == 1:
            ch = ch.lower()
            return ord(ch) - ord('a') + 1
    return None



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
