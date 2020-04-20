def firstMonthDay(month, year):
    """
    int, int -> str
    Precondition: year > 1583, 0 < month < 13

    Return the first weekday of month in this year

    >>> firstMonthDay(10, 2018)
    'mon'
    """

    assert (month > 0 and month < 13 and year > 1583)

    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # description of algorithm was taken from https://ru.wikibooks.org
    # I changed it first day in month
    a = (14 - month) // 12
    y = year - a
    m = month + 12 * a - 2
    day_index = (((1 + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12)) % 7) - 1
    return weekdays[day_index]

def monthType(month, year):
    """
    int, int -> int
    Precondition: year > 1583, 0 < month < 13

    Return amount of days in month in this year

    >>> monthType(9, 2014)
    30
    >>> monthType(2, 2016)
    29
    >>> monthType(2, 2018)
    28
    """

    assert (month > 0 and month < 13 and year > 1583)

    days_amount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and year % 4 == 0:
        return 29
    return days_amount[month - 1]

def getCalendar(month, year):
    """
    (int, int) -> str
    Precondition: year > 1583, 0 < month < 13

    Return a string representing a calendar for given month and year

    month : an integer in range[1 , 12]
    year : an integer (strictly speaking the algorithm in getWeekday works
           correctly only for Gregorian calendar, so year must be greater
           than 1583)
    when arguments are invalid raises AssertionError with corresponding message

    >>> print(getCalendar(8 , 2015))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """

    assert (month > 0 and month < 13 and year > 1583)

    first_day = firstMonthDay(month, year)
    days_in_month = monthType(month, year)
    weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    empty_dates = weekdays.index(first_day)
    result_list = []

    first_weekdays = weekdays[:empty_dates]
    for i in first_weekdays:
        next_date = 8 - empty_dates + first_weekdays.index(i)
        i += '   '
        while next_date <= days_in_month:
            i += (str(next_date) + ' ')
            if(next_date < 10 and first_day != 'sat' and first_day != 'sun') or\
            (next_date == 9 and first_day == 'sun'):
                i += ' '
            next_date += 7
        i = i[:-1] + '\n'
        result_list.append(i)

    last_weekdays = weekdays[empty_dates:]
    for i in last_weekdays:
        next_date = 1 + last_weekdays.index(i)
        i += ' '
        while next_date <= days_in_month:
            i += (str(next_date) + ' ')
            if next_date < 10 and next_date > 7 \
            and first_day != 'sat' and first_day != 'sun':
                i += ' '
            next_date += 7
        i = i[:-1] + '\n'
        result_list.append(i)

    return ''.join(result_list)[:-1]



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
