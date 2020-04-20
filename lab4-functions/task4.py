def egg_carton_box(eggs):
    """
    (int) -> int
    Precondition: eggs > 0
    Return the smallest number of boxes in which this number of eggs can be packed
    >>> egg_carton_box(12)
    2
    >>> egg_carton_box(28)
    3
    """
    count = 0
    while(eggs > 0):
        if eggs <= 6:
            if eggs <= 4:
                eggs -= 4
                count += 1
            else:
                eggs -= 6
                count += 1
        else:
            eggs -= 10
            count += 1
    return count


# print(egg_carton_box(28))
import doctest
print(doctest.testmod())
