
import random
import string

class options:
  def __init__(self, length, symbols, numbers):
    self.length = length
    self.symbols = symbols
    self.numbers = numbers





request = options(16, False, False)
characters = string.ascii_letters

   

def set_characters(symbols: bool, numbers: bool):
    characters = string.ascii_letters

    if symbols and numbers:
        return characters + string.punctuation + string.digits
    elif symbols:
        return characters + string.punctuation
    elif numbers:
        return characters + string.digits
    
characters_len = len(characters)

characters_list = list(characters)

x = []

for i in range(23):
   
   

   x.append(characters_list[random.randrange(characters_len)])


    

print(x)
    



       


    
    




  