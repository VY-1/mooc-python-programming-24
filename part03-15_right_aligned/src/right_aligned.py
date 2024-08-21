# Write your solution here

word = input("Please type in a string: ")

length_left = 20-len(word)
star = "*"

print(star*length_left + word)