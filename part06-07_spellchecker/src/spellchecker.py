# write your solution here
user_input = input("Write text: ")
words = user_input.split(" ")


def read_file(file_input):
    with open(file_input) as dictionary_file:
        word_list = []
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

        print(output)

read_file("src/wordlist.txt")