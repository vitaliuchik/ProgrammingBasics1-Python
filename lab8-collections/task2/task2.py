def common_names(female_names, male_names):
    """
    list(str), list(str) -> set(str)

    Return set of common name in two lists

    >>> common_names(['Linda', 'Shelby'], ['Shelby', 'James'])
    {'Shelby'}
    """
    male = set(male_names)
    female = set(female_names)
    return male.intersection(female)



def names_read(file_name):
    """
    str -> list

    Return list of lines in file
    """
    f = open(file_name, encoding='utf-8')
    return [name[:-1] for name in f.readlines()]


print(common_names(names_read('female.txt'), names_read('male.txt')))
import doctest
print(doctest.testmod())
