# write your solution here
import difflib
from difflib import get_close_matches

user_input = input("Write text: ")
words = user_input.split(" ")


def read_file(file_input):
    with open(file_input) as dictionary_file:
        word_list = []
        suggested_word_list = {}
        for word in dictionary_file:
            word = word.replace("\n", "")
            word_list.append(word)

        output = ""
        for word in words:
            if word.lower() in word_list:
                output +=word
            else:
                output += "*"+word+"*"
            output += " "

            if word.lower() not in word_list:
                suggested_word_list[word.lower()] = get_close_matches(word.lower(), word_list)

        print(output)
        print("suggestions:")
        for key, word in suggested_word_list.items():
            print(f"{key}: {", ".join(word)}")

read_file("src/wordlist.txt")