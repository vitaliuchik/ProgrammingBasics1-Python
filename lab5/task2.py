def egg_carton_box(eggs):
    """
    (int) -> list
    Precondition: eggs > 0
    Return list of boxes (the smallest amount) in which this number of eggs can be packed
    >>> egg_carton_box(22)
    [6, 6, 10]
    >>> egg_carton_box(28)
    [10, 10, 10]
    """
    boxes_lst = []
    while(eggs > 0):
        if eggs <= 6:
            if eggs <= 4:
                eggs -= 4
                boxes_lst.append(4)
            else:
                eggs -= 6
                boxes_lst.append(6)
        elif eggs == 11 or eggs == 12:
            eggs -= 12
            boxes_lst.append(6)
            boxes_lst.append(6)
        else:
            eggs -= 10
            boxes_lst.append(10)
        boxes_lst.sort()
    return boxes_lst


print(egg_carton_box(14))
import doctest
print(doctest.testmod())
