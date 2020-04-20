def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> print(convert_to_column("Revenge is a dish that tastes best when served cold."))
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> print(convert_to_column("Never hate your enemies. It affects your judgment."))
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> print(convert_to_column(2015))
    None
    """
    try:
        result_str = ''
        s = s.lower().split()
        for word in s:
            for letter in word:
                if letter.isalpha():
                    result_str += letter
            result_str += '\n'
        return result_str[:-1]
    except AttributeError:
        return None



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
