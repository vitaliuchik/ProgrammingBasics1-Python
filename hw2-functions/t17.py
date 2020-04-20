def number_of_occurence(lst, s):
    """
    (list, str) -> int
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
    2
    >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], "1")

    """
    if isinstance(lst, list) and isinstance(s, str):
        result_count = 0
        for i in lst:
            if not isinstance(i, str):
                return None
            else:
                result_count += i.count(s)
        return result_count

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
