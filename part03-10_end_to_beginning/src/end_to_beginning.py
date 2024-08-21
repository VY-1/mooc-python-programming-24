# Write your solution here

word = input("Please type in a string: ")

last_char_index = len(word)-1
while last_char_index >=0:
    print(word[last_char_index])
    last_char_index-=1
    
