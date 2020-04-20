def number_of_capital_letters(s):
    """
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    >>> number_of_capital_letters("ArithmeticError")
    '2'
    >>> number_of_capital_letters("EOFError")
    '4'
    >>> number_of_capital_letters(1)

    """
    if isinstance(s, str):
        capital_count = 0
        for letter in s:
            if letter.isupper():
                capital_count += 1
        return str(capital_count)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
