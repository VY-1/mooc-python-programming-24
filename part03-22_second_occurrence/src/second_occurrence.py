# Write your solution here

word = input("Please type in a string: ")
substring = input("Please type in a substring: ")

first_found_index = word.find(substring)

second_found_index = word[first_found_index + len(substring):].find(substring)

if first_found_index !=-1 and second_found_index !=-1:
    print(f"The second occurrence of the substring is at index {first_found_index + second_found_index + len(substring)}.")
else:
    print(f"The substring does not occur twice in the string.")