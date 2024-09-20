# Write your solution here

def read_file(file_in: str):
    contents = []
    with open(file_in) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            contents.append(line)

    return contents
def word_with_dot(search_word, word):
    
    for i in range(len(search_word)):
        if search_word[i] == ".":      #checking for edge case
            continue

        if search_word[i] != word[i]:
            return False    #word does not match if they are not the same

    return True



def find_words(search_term: str):
    found_list = []
    words = read_file("words.txt")
    for word in words:
        if "." in search_term and len(search_term) == len(word):
            found_word = word_with_dot(search_term, word)
            if found_word:      #If True, add to found_list
                found_list.append(word)
        elif search_term.startswith('*'):
            if word.endswith(search_term[1:]):
                found_list.append(word)

        elif search_term.endswith('*'):
            if word.startswith(search_term[:-1]):
                found_list.append(word)
        else:
            if search_term == word:
                found_list.append(word)
    return found_list
if __name__ == "__main__":
    print(word_with_dot("ca.s", "cata"))
    print(word_with_dot("ca.s", "cats"))
    print(word_with_dot("c.d.", "cade"))

    print(find_words("*vokes"))