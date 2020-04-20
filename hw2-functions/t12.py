def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    >>> exclude_letters("aaabb", "b")
    'aaa'
    >>> exclude_letters("abcc", "cczzyy")
    'ab'
    >>> exclude_letters(2015, "sasd")

    """
    if isinstance(s1, str) and isinstance(s2, str):
        result_str = ''
        for letter in s1:
            if not letter in s2:
                result_str += letter
        return result_str

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
