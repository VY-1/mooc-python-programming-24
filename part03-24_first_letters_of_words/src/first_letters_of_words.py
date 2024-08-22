# Write your solution here
sentence = input("Please type in a sentence: ")

words = sentence.split(" ")     # split sentence by " " and store as list of words

for word in words:
    print(word[0])      #print char at index 0