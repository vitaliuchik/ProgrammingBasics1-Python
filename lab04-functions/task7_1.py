def four_line_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    (float, float, float, float, float, float, float, float) -> float
    Precondition: k1 = k2
    Return area of the quadrangle
    >>> four_line_area(0, 0, 0, 1, 1, 0, -1, 4)
    3.0
    >>> four_line_area(0, 0, 0, 1, 0, 0, -1, -4)
    0
    """
    if (k1 != k2):
        return None
    if ((k1 == k2 and (k1 == k3 or k1 == k4)) or (k1 == k3 and k1 == k4) or (k2 == k3 and k2 == k4)):
        return 0
    (x1, y1) = line_intersection(k1, c1, k3, c3)
    (x2, y2) = line_intersection(k1, c1, k4, c4)
    (x3, y3) = line_intersection(k2, c2, k3, c3)
    (x4, y4) = line_intersection(k2, c2, k4, c4)

    a = distance(x1, y1, x2, y2)
    b = distance(x3, y3, x4, y4)

    h = high(k1, c1, x3, y3)

    return quadrangle_area(a, b, h)


def line_intersection(k1, c1, k2, c2):
    """
    (float, float, float, float) -> tuple
    Return the point of intersection
    >>> line_intersection(0.0, 0.0, 1.0, 0.0)
    (0.0, 0.0)
    """
    if k1 == k2:
        return None
    x = round((c1 - c2) / (k2 - k1), 2)
    y = round(k1 * ((c1 - c2)/(k2 - k1)) + c1, 2)
    return (x, y)


def distance(x1, y1, x2, y2):
    """
    (float, float, float, float) -> float
    Return the distance between two points
    >>> distance(1.0, 1.0, 3.0, 1.0)
    2.0
    """
    return round(((x2-x1)**2 + (y2-y1)**2)**0.5, 2)


def quadrangle_area(a, b, h):
    """
    (float, float, float) -> float
    Return area of the quadrangle
    >>> quadrangle_area(6.0, 4.0, 5.0)
    25.0
    """
    return round((a+b) / 2 * h, 2)


def high(k, c, x, y):
    """
    (float, float, float, float) -> float
    Return distance between point(x, y) and line(Ax + By + C = 0  <=>  kx - y + c = 0 )
    """
    return round(abs(k*x - y + c) / (k**2 + 1)**0.5, 2)


print(four_line_area(0, 0, 0, 1, 1, 0, -1, 4))
