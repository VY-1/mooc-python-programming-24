# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    ascii_char = ""
    punc = ""
    all_other = ""
    for char in my_string:
        if char in ascii_letters:
            ascii_char +=char
        elif char in punctuation:
            punc +=char
        else:
            all_other += char
    return (ascii_char, punc, all_other)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])

    # will return tuple
    ascii_chars, punc_char, other_char = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(ascii_chars)
    print(punc_char)
    print(other_char)