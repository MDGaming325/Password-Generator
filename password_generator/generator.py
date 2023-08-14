import random
import string


class options:
    def __init__(self, length, symbols, numbers):
        self.length = length
        self.symbols = symbols
        self.numbers = numbers


def set_characters(symbols: bool, numbers: bool):
    characters = string.ascii_letters

    if symbols and numbers:
        return characters + string.punctuation + string.digits
    elif symbols:
        return characters + string.punctuation
    elif numbers:
        return characters + string.digits


y = set_characters(True, True)
x = []

request = options(16, True, True)

characters_len = len(y)
characters_list = list(y)


def create_arr():

    for i in range(request.length):
        x.append(characters_list[random.randrange(characters_len)])

    string = ''.join(x)

    print(string)


