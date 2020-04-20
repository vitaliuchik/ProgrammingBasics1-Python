def borsch_ingredients(portions):
    """
    (int) -> list
    Precondition: portions > 0
    Return list of tuples with ingredients and weight
    >>> borsch_ingredients(8)
    [('яловичина', 700), ('буряк', 500), ('картопля', 500), ('морква', 200), ('цибуля', 200), ('помідори', 300), ('капуста', 300)]
    >>> borsch_ingredients(10)
    [('яловичина', 900), ('буряк', 700), ('картопля', 700), ('морква', 300), ('цибуля', 300), ('помідори', 400), ('капуста', 400)]
    """
    import math
    menu = ['яловичина', 'буряк', 'картопля', 'морква', 'цибуля', 'помідори', 'капуста']
    weight = [700, 500, 500, 200, 200, 300, 300]
    result_weight = []

    for ingredient in weight:
        result_weight.append(math.ceil(ingredient * portions / 8 / 100) * 100)

    return [(menu[i], result_weight[i]) for i in range(7)]


import doctest
print(doctest.testmod())
