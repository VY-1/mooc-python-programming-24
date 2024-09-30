# Write your solution here

from string import ascii_letters, digits
def change_case(orig_string: str)->str:
    new_word = ""
    for char in orig_string:
        if char.islower():
            new_word += char.upper()
        else:
            new_word += char.lower()

    return new_word

def split_in_half(orig_string: str)-> tuple:
    new_word = tuple()
    first = ""
    second = ""
    half = len(orig_string)//2      #round down integer

    for i, char in enumerate(orig_string):

        if i < half:
            first += char
        else:
            second += char
    new_word = (first, second)
    return new_word

def remove_special_characters(orig_string: str)-> str:
    new_word = ""
    allowed_char = f"{ascii_letters}{digits} "
    for char in orig_string:
        if char in allowed_char:
            new_word += char

    return new_word


if __name__ == "__main__":


    print(change_case("The Word is Cool"))
    print(split_in_half("Well hello there!"))

    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))