def division_of_two(number, divisor):
    """
    (int, int) -> bool
    Precondition: 1 < divisor < 10
    Check whether divisor is divisor of number
    >>> division_of_two(81, 9)
    True
    >>> division_of_two(81, 2)
    False
    """
    if (divisor < 2 or divisor > 9):
        return False
    if (number % divisor == 0):
        return True
    return False


print(division_of_two(18, 3))
import doctest
print(doctest.testmod())
