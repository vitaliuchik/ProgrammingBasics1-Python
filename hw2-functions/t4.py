def type_by_angles(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such angles, then function should return None.

    >>> type_by_angles(60, 60, 60)
    'acute triangle'
    >>> type_by_angles(90, 30, 60)
    'right angled triangle'
    >>> type_by_angles(90.0, 30, 60)
    'right angled triangle'
    >>> type_by_angles(2015, 2015, 2015)

    >>> type_by_angles(-1, 90, 91)

    """
    if (a > 0 and b > 0 and c > 0 and a + b + c == 180):
        if (a == 90 or b == 90 or c == 90):
            return 'right angled triangle'
        elif (a > 90 or b > 90 or c > 90):
            return 'obutuse triangle'
        return 'acute triangle'


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
