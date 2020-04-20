l = ['sdth', 'srag', 'wesa', 'gapunovich']


def surname_list(lst):
    """
    (list) -> None
    Print surnames and random digits in file surnames.txt
    """
    import random
    output = open('surnames.txt', 'w')
    for surname in lst:
        print(surname + str(random.randint(1, 9)), file=output)
    output.close()


surname_list(l)
