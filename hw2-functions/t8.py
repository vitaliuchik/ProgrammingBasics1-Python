def number_of_sentences(s):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    '1'
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    '2'
    >>> number_of_sentences(2015)

    """
    # if isinstance(s, str):
    #     sentence_count = 1
    #     for i in range(2,len(s)):
    #         if not s[i-2].isalpha() and s[i].isupper():
    #             sentence_count += 1
    #     return str(sentence_count)
    if isinstance(s, str):
        sentence_count = s.count('.') + s.count('!') + s.count('?')
        return str(sentence_count)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
