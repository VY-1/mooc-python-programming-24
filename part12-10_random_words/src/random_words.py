# Write your solution here:
from random import choice


def word_generator(characters: str, length: int, amount: int):
    char_string = ""
    for i in range(amount):

        for j in range(length):
            char_string += choice(characters)
        yield char_string
        char_string = ""

# def word_generator(letters: str, length: int, amount:int):
#     return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))
 

if __name__=="__main__":
    wordgen = word_generator("abcdefg", 2, 5)
    for word in wordgen:
        print(word)