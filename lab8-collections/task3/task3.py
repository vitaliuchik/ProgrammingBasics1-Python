def dict_reader_tuple(file_dict):
    """
    >>> len(dict_reader_tuple('cmudict'))
    133737
    """
    f = open(file_dict, encoding='utf-8')
    words = f.readlines()
    f.close()
    words = [word.split() for word in words]
    result = [(el[0], int(el[1]), el[2:]) for el in words]
    return result

def dict_reader_dict(file_dict):
    """
    >>> len(dict_reader_dict('cmudict'))
    123455
    """
    f = open(file_dict, encoding='utf-8')
    words = f.readlines()
    f.close()
    dictionary = dict()
    words = [word.split() for word in words]
    for word in words:
        dictionary[word[0]] = dictionary.get(word[0], set())
        dictionary[word[0]].add(tuple(word[2:]))
    return dictionary

def dict_invert(dictionary):
    """
    >>> len(dict_invert(dict_reader_dict('cmudict')))
    5
    """
    for el in dictionary.keys():
        dictionary[el] = tuple(dictionary[el])

    tuple_dict = tuple(dictionary.items())
    result_dict = dict()
    for word in tuple_dict:
        result_dict[len(word[1])] = result_dict.get(len(word[1]), set())
        result_dict[len(word[1])].add(word)
    return result_dict

# print(len(dict_invert(dict_reader_dict('cmudict'))))
# print(len(dict_reader_dict('cmudict')))

import doctest
print(doctest.testmod())
