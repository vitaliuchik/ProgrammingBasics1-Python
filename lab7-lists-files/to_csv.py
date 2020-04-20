def read_input_file(url, number):
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """

    import urllib.request
    f = urllib.request.urlopen(url)
    text = f.readlines()
    result_list = []
    for i in range(len(text)):
        text[i] = text[i].strip().decode('utf-8')
        text[i] = text[i].replace('\t', ' ')
        text[i] = text[i].split()
    for i in range(len(text)):
        if text[i][0].isdigit():
            el = text[i]
            document = ''
            if text[i + 6][0] == '—':
                document = text[i + 6][-1]
            elif text[i + 7][0] == '—':
                document = text[i + 7][-1]
            name = ' '.join([el[1], el[2], el[3]])
            s = [el[0], name, document, el[6], text[i + 3][-1] ]
            result_list.append(s)

    return result_list[:number]


def write_csv_file(url):
    """
    str -> None

    Write dataset into total.f_csv

    >>> write_csv_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt')
    """

    f_csv = open('total.csv', 'w', encoding='utf-8')
    f_csv.write(u'№,ПІБ,Д,Заг.бал,С.б.док.осв.')
    f_csv.write('\n')
    lst = read_input_file(url, 70)
    for i in lst:
        f_csv.write(','.join(i))
        f_csv.write('\n')
    
    f_csv.close()



write_csv_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt')

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
