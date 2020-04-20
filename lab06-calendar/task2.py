def dyvo_insert(sentence, flag):
    """
    (str, str) -> str
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert('lol df lol', 'lo')
    'диво lol df диво lol'
    >>> dyvo_insert('lol dflo olol', 'am')
    'lol dflo olol'
    """
    count = 0
    while True:
        if sentence[count:count + 2] == flag:
            sentence = sentence[:count] + "диво " + sentence[count:]
            count += 6
        else:
            count += 1
        if count == len(sentence):
            return sentence.lower()

print(dyvo_insert('lolo', 'am'))
import doctest
print(doctest.testmod())
