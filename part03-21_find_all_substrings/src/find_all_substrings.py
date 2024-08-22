# Write your solution here

word = input("Please type in a word: ")

character = input("Please type in a character: ")


while True:
    char_index = word.find(character)   # Char at index
    
    if char_index ==-1 or len(word) - char_index < 3:
        break
    
    print(word[char_index: char_index+3])
        
    char_index+=1           #increase char_index by 1
    word = word[char_index:]

        