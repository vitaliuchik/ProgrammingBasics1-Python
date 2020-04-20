def one_swap_sorting(sequence):
    """
    str -> bool

    Reutrn if sequence needs only one swap to be sorted

    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """
    changes_count = 0
    sorted_sequence = sequence[:]
    sorted_sequence.sort()
    for i in range(len(sequence)):
        if sequence[i] != sorted_sequence[i]:
            changes_count += 1
    if changes_count == 2:
        return True
    return False


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
