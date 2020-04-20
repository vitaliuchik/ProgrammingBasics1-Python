def polynomials_multiply(polynom1, polynom2):
    """
    list(int), list(int) -> list(int)

    Return coeficients  of polynomials_multiply

    >>> polynomials_multiply([2], [3])
    [6]
    >>> polynomials_multiply([2, -4],[3, 5])
    [6, -2, -20]
    >>> polynomials_multiply([2, 0, -4],[3, 0, 2, 0])
    [6, 0, -8, 0, -8, 0]
    """
    result_polynom = [0 for i in range(len(polynom1) + len(polynom2) - 1)]
    for i in range(len(polynom1)):
        for j in range(len(polynom2)):
            result_polynom[i + j] += polynom1[i] * polynom2[j]
    return result_polynom



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
