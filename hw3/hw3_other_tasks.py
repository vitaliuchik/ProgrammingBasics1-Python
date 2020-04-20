def is_power_of_two(val):
    """
    (int) -> bool

    Determine if a number is a power of two.

    >>> is_power_of_two([0])

    >>> is_power_of_two("0")

    >>> is_power_of_two(0)
    False
    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(15)
    False
    >>> is_power_of_two(16)
    True
    """
    if not isinstance(val, int):
        return None
    while val != 1:
        val /= 2
        if val - int(val) != 0.0 or val == 0:
            return False
    return True


def has_unique_chars(string):
    """
    (str) -> bool

    An algorithm to determine if a string has all unique characters.

    >>> has_unique_chars(None)
    False
    >>> has_unique_chars('')
    True
    >>> has_unique_chars('foo')
    False
    >>> has_unique_chars('bar')
    True
    """
    if not isinstance(string, str):
        return False
    chars = tuple(char for char in string)
    unique = set(chars)
    if len(chars) == len(unique):
        return True
    return False

def compress(string):
    """
    (str) -> str

    Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.

    >>> compress(None)

    >>> compress('')
    ''
    >>> compress('AABBCC')
    'AABBCC'
    >>> compress('AAABCCDDDDE')
    'A3BC2D4E'
    >>> compress('BAAACCDDDD')
    'BA3C2D4'
    >>> compress('AAABAACCDDDD')
    'A3BA2C2D4'
    """
    if not isinstance(string, str):
        return None
    result = ''
    amount = 1
    for i in range(len(string) - 1):
        current = string[i]
        if string[i + 1] == current:
            amount += 1
        else:
            if amount == 1:
                result += current
            else:
                result += (current + str(amount))
            amount = 1
        if i == len(string) - 2:
            if amount == 1:
                result += string[i + 1]
            else:
                result += (string[i + 1] + str(amount))
    if len(result) == len(string):
        return string
    return result

import doctest
print(doctest.testmod())
