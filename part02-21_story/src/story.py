# Write your solution here

all_string = ""
last_word = ""

while True:
    word = input("Please type in a word: ")
    
    if word == "end" or word == last_word:
        break
    
    all_string += word + " "
    last_word = word
    

print(all_string)