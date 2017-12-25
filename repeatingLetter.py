def is_isogram(string):
    letterCount = set([])
    for letter in string:
        if letter in letterCount:
            return False
        letterCount.add(letter)
    return True



is_isogram("Dermatoglyphics")