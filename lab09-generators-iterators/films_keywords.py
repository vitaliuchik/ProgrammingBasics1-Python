def film_analysis():
    """
    Analise keywords.list 
    """
    print_intro()
    keywords, film_keywords = input_from_file()
    keyw1, keyw2 = freq_keywords(keywords)
    number_films = find_films(film_keywords, keyw1, keyw2)
    print_report(number_films, keyw1, keyw2)



def print_intro():
    print("This program find number of films")
    print("that use two keywords with maximal frequency.")
    print("This program use data from imdb database file keywords.list.")


def keywords_generator(f):
    """
    Keywords generator
    """

    data = f.readline()
    while not data.startswith("5: Sub"):
        data = f.readline().strip()
        yield data


def input_from_file():
    """
    Returns the list of tuple and generator of dictionary
    """

    file_name = input("Please type the file name and path to file if need: ")
    f = open(file_name, encoding='utf-8', errors='ignore')
    data = f.readline()
    while not data.startswith("   keywords in use:"):
        data = f.readline()

    keywords = [w.split("\t") for w in keywords_generator(f)]
    keywords = [(int(w.split()[1][1:-1]), w.split()[0])
                for lst1 in keywords[:-1]
                for w in list(filter(lambda w: w, lst1))]

    data = f.readline()
    while not data.startswith("8: THE"):
        data = f.readline()

    film_keywords = {}
    for line in f:
        film, keyword = line.strip().split("\t")[0], \
                        line.strip().split("\t")[-1]
        film_keywords[keyword] = film_keywords.get(keyword, list())
        film_keywords[keyword].append(film)

    return keywords, film_keywords


def freq_keywords(keywords):
    """
    Find and return two keywords
    (find the indexes of two maximum items in the tuple list)
    """
    (keyw1, keyw2) = (keywords[find_two_biggest1(keywords)[i]][1]
                      for i in range(2))

    return keyw1, keyw2


def find_two_biggest1(lst):
    """ (list of tuple) -> tuple of (int, int)
    Return a tuple of the indices of the two tuple with biggest first values
    in list lst.
    >>> find_two_biggest([(1, '102-convictions'),
                          (1, '102-pushups'),
                          (3, '1020s'),
                          (1, '102nd-century'),
                          (2, '102nd-street-manhattan-new-york-city')])
    (2, 4)
    """
    # Find the index of the max item in lst
    #     Get the max item in lst
    #     Find the index of that max item
    # Remove that item from the list
    # Find the index of the new max item in the list
    # Put the biggest item back in the list
    # If necessary, adjust the second index
    #     Fix max2 in case it was affected by the reinsertion:
    #     If max1 comes before max2, add 1 to max2
    # Return the two indices

    # Find the index of the max and remove that item
    biggest = max(lst)
    max1 = lst.index(biggest)
    lst.remove(biggest)
    # Find the index of the new max
    next_biggest = max(lst)
    max2 = lst.index(next_biggest)
    # Put biggest back into lst
    lst.insert(max1, biggest)
    # Fix max2 in case it was affected by the reinsertion
    if max1 <= max2:
        max2 += 1

    return (max1, max2)


def find_films(film_keywords, keyw1, keyw2):
    """
    Return number of films that using keywords
    """
    common_films = list(set(film_keywords[keyw1]) & set(film_keywords[keyw2]))
    return sum([len(film_keywords[keyw1]), len(film_keywords[keyw2])]) - \
                len(common_films)


def print_report(number_films, *args):
    """
    Print a report on the number of films
    """
    print("\nFilms analysis result")
    print("Keywords {0} and {1} are using".format(*args))
    print("in {0} films".format(number_films))


if __name__ == '__main__':
    film_analysis()
