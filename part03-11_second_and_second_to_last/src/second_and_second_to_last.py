# Write your solution here

word = input("Please type in a string: ")

second_char = word[1]
second_to_last_char = word[len(word)-2]

if second_char == second_to_last_char:
    print(f"The second and the second to last characters are {second_char}")
else:
    print(f"The second and the second to last characters are different")