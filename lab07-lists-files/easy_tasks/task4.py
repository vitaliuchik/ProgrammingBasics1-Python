def happy_number(number):
    """
    (int) -> bool
    Check if number is happy
    Precondition: 0 < number < 99999999

    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    >>> happy_number(191234)
    True
    """
    reversed = str(number)[::-1]
    if len(reversed) != 8:
        reversed += ('0' * (8 - len(reversed)))
    left_sum = 0
    right_sum = 0
    for i in range(4):
        left_sum += int(reversed[i])
        right_sum += int(reversed[i + 4])
    if right_sum == left_sum:
        return True
    return False

def count_happy_numbers(n):
    """
    (int) -> int
    Return amount of happy tickets in serias
    Precondition: 0 < n < 99999999

    >>> count_happy_numbers(1000)
    0
    >>> count_happy_numbers(100000)
    714
    """
    happy_tickets_count = 0
    for i in range(1, n + 1):
        if happy_number(i):
            happy_tickets_count += 1
    return happy_tickets_count


def happy_numbers(m,n):
    """
    (int) -> list
    Return list of happy tickets in range
    Precondition: 0 < m, n < 99999999

    >>> happy_numbers(1000, 10000)
    []
    >>> happy_numbers(190000, 190100)
    [190019, 190028, 190037, 190046, 190055, 190064, 190073, 190082, 190091]
    """
    happy_tickets = []
    for i in range(m, n + 1):
        if happy_number(i):
            happy_tickets.append(i)
    return happy_tickets
