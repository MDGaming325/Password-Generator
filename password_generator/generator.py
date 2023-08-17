import random
import string
from django import forms
from django.db import models



def set_characters(symbols: bool, numbers: bool):
    characters = string.ascii_letters

    if symbols and numbers:
        return characters + string.punctuation + string.digits
    elif symbols:
        return characters + string.punctuation
    elif numbers:
        return characters + string.digits


def gen_password(length:int, symbols:bool, numbers:bool):
    
    x = []

    loaded_characters = set_characters(symbols, numbers)
    characters_len = len(loaded_characters)
    characters_list = list(loaded_characters)

    for i in range(length):
        x.append(characters_list[random.randrange(characters_len)])

    string = ''.join(x)

    return string
