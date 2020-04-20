l = ['SS', 'SP', 'PR', 'PS']


def rps_game(lst):
    """
    (list) -> list
    Return list of tuples with results
    >>> rps_game(['SS', 'RS', 'PS'])
    [(False, False), (True, False), (False, True)]
    >>> rps_game(['PR'])
    [(True, False)]
    """

    def game(match):
        """
        (str) -> tuple
        Return tuple with result
        >>> game('SS')
        (False, False)
        >>> game('PR')
        (True, False)
        >>> game('SR')
        (False, True)
        """
        match = match.upper()
        if (match == 'SS' or match == 'RR' or match == 'PP'):
            return (False, False)
        elif (match == 'SP' or match == 'PR' or match == 'RS'):
            return (True, False)
        else:
            return (False, True)

    return [game(result) for result in lst]


print(rps_game(l))
import doctest
print(doctest.testmod())
