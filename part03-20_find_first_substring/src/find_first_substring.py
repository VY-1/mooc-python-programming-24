# Write your solution here

word = input("Please type in a word: ")

char = input("Please type in a character: ")

char_index = word.find(char)    #the index where the char first found

if char_index + 3 <= len(word):
    print(word[char_index: char_index +3])  # print word with index of char_index to char_index +3