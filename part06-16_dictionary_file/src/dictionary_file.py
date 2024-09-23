# Write your solution here

def write_file(file_out: str, word:str):
    with open(file_out, "a") as new_file:
        new_file.write(word)

def read_file(file_in: str, search_word: str):
    with open(file_in) as new_file:
        word_list = []
        for line in new_file:
            line = line.replace("\n", "")
            if search_word in line:
                word_list.append(line)
        return word_list

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 3:
        break
    if function == 1:
        word_finnish = input("The word in Finnish: ")
        word_english = input("The word in English: ")
        word = f"{word_finnish};{word_english}\n"
        write_file("dictionary.txt", word)
        print("Dictionary entry added")
    if function == 2:
        search_term = input("Search term: ")
        word_list = read_file("dictionary.txt", search_term)
        for word in word_list:
            word = word.replace(";", " - ")
            print(word)
print("Bye!")

