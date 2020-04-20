def  grade_count(grades):
    """
    list[int, int, int, int, int] -> tuple
    Return average grade and ECTS grade
    >>> grade_count([85, 90, 67, 70, 87])
    (79.8, 'C')
    >>> grade_count([97, 93, 84, 78, 80])
    (86.4, 'B')
    >>> grade_count([107, 93, 84, 78, 80])
    (None, None)
    """
    sum = 0
    for grade in grades:
        if grade < 0 or grade > 100:
            return (None, None)
        sum += grade
    sum = round(sum / 5, 2)
    if sum < 60:
        return (sum, 'F')
    elif sum < 67:
        return (sum, 'E')
    elif sum < 75:
        return (sum, 'D')
    elif sum < 82:
        return (sum, 'C')
    elif sum < 90:
        return (sum, 'B')
    elif sum <= 100:
        return (sum, 'A')


import doctest
print(doctest.testmod())
print(grade_count([90, 87, 93, 68, 71]))
