# Write your solution here
from random import choice, shuffle
from string import ascii_letters, punctuation, digits, ascii_lowercase


def generate_strong_password(length: int, has_number: bool, has_symbol: bool):
    letters = ascii_lowercase
    syms = "!?=+-()#"
    nums = digits
    possible_pass = ""
    password = ""
    password = f"{choice(letters)}"  #at least one lowercase letter
    length -=1
    if has_number and has_symbol:
        password += f"{choice(nums)}{choice(syms)}"
        length -=2
        possible_pass = f"{letters}{nums}{syms}"
    elif has_number:
        password += f"{choice(nums)}"
        length -=1
        possible_pass = f"{letters}{nums}"
    elif has_symbol:
        password += f"{choice(syms)}"
        length -=1
        possible_pass = f"{letters}{syms}"
    else:
        possible_pass = f"{letters}"
    for _ in range(length):
            password += f"{choice(possible_pass)}"
            
    pass_list = list(password)
    shuffle(pass_list)
    rand_pass = "".join(pass_list)
    return rand_pass


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
