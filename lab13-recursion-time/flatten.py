def flatten(lst):
    """
    (list -> list)
    Returns opened list in the same order
    """
    if not isinstance(lst, list):
        return lst
    result = []
    for el in lst:
        if isinstance(el, list):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


    
