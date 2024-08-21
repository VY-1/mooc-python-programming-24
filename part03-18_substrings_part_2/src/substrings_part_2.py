# Write your solution here

word = input("Please type in a string: ")

word_length = len(word)
count = len(word)-1

while count >= 0:
    print(word[count: word_length])
    count-=1