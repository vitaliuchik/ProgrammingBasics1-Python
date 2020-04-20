def generate_grid():
    """
    () -> list(list)

    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    import random
    import string
    return [[random.choice(string.ascii_uppercase) for j in range(3)] \
            for i in range(3)]


def get_words(words, letters):
    """
    (list, list) -> list()

    Checks the words with rules and returns a new list of words.
    """
    words = read_dict(words)
    letters_str = ''.join(letters)
    letters_dict = dict(set((i, letters_str.count(i)) for i in letters_str))
    main_let = letters_str[4]
    new_words = [new for new in words if (len(new) > 3 and main_let in new and]
    new_words_dict = [dict(set((i, word.count(i)) for i in word)) for word in new_words]

    result_words = []
    for i in range(len(new_words_dict)):
        word = new_words_dict[i]
        flag = False
        for letter in word.keys():
            if letter in letters_dict.keys():
                if word[letter] <= letters_dict[letter]:
                    flag = True
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            result_words.append(new_words[i])

    return result_words



def read_dict(f):
    """
    (str) -> list

    Reads the file (f) and returns a list with the words from this file.
    """
    f = open(f, encoding='utf-8')
    words = f.readlines()
    f.close()
    return [word[:-1] for word in words]



def get_user_words():
    """
    () -> list

    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = []
    while True:
        word = str(input())
        if word:
            words.append(word)
        else:
            break
    return words


def get_pure_user_words(user_words, letters, words_from_dict):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass


# get_words(['lol', 'aaaa', 'abcd', 'aard'], [['a','a','a'], ['r','d','f'], ['d','a','x']])
print(get_words('en', [el for el in 'vhtdsrael']))

# 'slav', 'sedat', 'shel'
