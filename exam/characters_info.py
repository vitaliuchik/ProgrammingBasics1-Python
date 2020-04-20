def input_data(path):
    """
    str -> list

    Returns the list of characters from the file.
    """
    f = open(path, encoding='utf-8')
    lines = f.readlines()
    f.close()
    return [line[:-1] for line in lines]

    
def row_extend(row):
    """
    list -> list

    Returns the extended row with sorted vowels by their frequency in the row.
    """
    row = row.lower()
    letters = ['a','e','i', 'o', 'u']
    lst = [(letters[i], row.count(letters[i])) \
           for i in range(5) if row.count(letters[i]) != 0]
    lst.sort(key=lambda x: x[1])
    for i in range(len(lst)):
        row += lst[i][0]
    return row
    

  
def characters_info(in_path, out_path):
    """
    str, str -> None

    The main function that reads the data from the file, processes it and 
    outputs to the other file.
    """    
    lines = input_data(in_path)
    f = open(out_path, 'w', encoding='utf-8')
    for line in lines:
        print(row_extend(line), file=f)
    f.close()
    
characters_info('text_1.txt', 'text.txt')
