def number_generator(number, digit, position):
    """
    (int, int, int) -> int
    Precondition: 0 <= digit <= 9 , position > 0
    Return number with changed digit on position
    >>> number_generator (3746, 5, 0)
    3746
    >>> number_generator (3746, 5, 1)
    3756
    >>> number_generator (3746, 5, 2)
    3746
    >>> number_generator (3746, 5, 3)
    5746
    >>> number_generator (3746, 5, 4)
    53746
    >>> number_generator (3746, 5, 7)
    50003746
    """

    reverse = str(number)[::-1]
    result = ''
    if (number < 0):
        reverse = reverse[:-1]
        result = '-'
    if position > len(reverse) - 1:
        result += (reverse + '0'*(position-len(reverse)) + str(digit))[::-1]
    elif int(reverse[position]) >= digit :
        result = number
    else:
        result += (reverse[:position] + str(digit) + \
        reverse[position + 1:])[::-1]
    return int(result)

print(number_generator (3746, 5, 0))
 # 3746

print(number_generator (3746, 5, 1))
 # 3756

print(number_generator (3746, 5, 2))
 # 3746

print(number_generator (3746, 5, 3))
 # 5746

print(number_generator (-3746, 7, 5))
 # 53746

print(number_generator (3746, 5, 7))
 # 50003746
