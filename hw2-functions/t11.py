def decrypt_message(encoded):
    """
    str -> str
    Replace all letters in string with previous letters in aplhabet. If argument isn't a string
    function should return None.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    'Revenge is a dish that tastes best when served cold.'
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Never hate your enemies. It affects your judgment.'
    >>> decrypt_message(2015)

    """
    if isinstance(encoded, str):
        decoded = ''
        for letter in encoded:
            if letter.isalpha():
                if ord(letter) == 97 or ord(letter) == 65:
                    decoded += chr(ord(letter) + 25)
                else:
                    decoded += chr(ord(letter) - 1)
            else:
                decoded += letter
        return decoded

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
