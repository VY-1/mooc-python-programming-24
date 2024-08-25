# Write your solution here
def first_word(word:str):
    new_word = word.split(" ")      #Split words based on spaces and put it in a list
    return new_word[0]              #returns word at index 0
def second_word(word:str):
    new_word = word.split(" ")
    return new_word[1]
def last_word(word:str):
    new_word = word.split(" ")
    return new_word[-1]             #returns word at the last index
    
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))