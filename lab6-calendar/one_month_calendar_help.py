def weekdayByNumber(number):
    """
    int -> str

    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekdayByNumber(3)
    'thu'
    """



def getWeekday(date):
    """
    str -> int
    Return an integer representing a weekday(0 represents monday and so on)
    read about algorithm at
    http://vidpo.net/de-znajti-metod-algoritm-viznachennja-dnja-tizhnja.html
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError with corresponding message

    >>> getWeekday("12.08.2015")
    2
    >>> getWeekday("28.02.2016")
    6
    """
    pass


def getCalendar(month, year):
    """
    (int, int) -> str

    Return a string representing a calendar for given month and year

    month : an integer in range[1 , 12]
    year : an integer (strictly speaking the algorithm in getWeekday works
           correctly only for Gregorian calendar, so year must be greater
           than 1583)
    when arguments are invalid raises AssertionError with corresponding message

    >>> get Calendar(8 , 2015)
    The calendar is:
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    pass


if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (getCalendar(month, year))
    except ValueError as err:
        print(err)
