import random
import string


def set_characters(symbols: bool, numbers: bool):
    characters = string.ascii_letters

    if symbols:
        characters += string.punctuation
    if numbers:
        characters += string.digits
    
    return characters + string.ascii_letters


def gen_password(length: int, symbols: bool, numbers: bool):

    x = []

    loaded_characters = set_characters(symbols, numbers)
    characters_len = len(loaded_characters)
    characters_list = list(loaded_characters)

    for i in range(length):
        x.append(characters_list[random.randrange(characters_len)])

    string = ''.join(x)

    return string
