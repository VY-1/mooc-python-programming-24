# Write your solution here
def  palindromes(word:str) -> bool:
    reverse_word = word[::-1]       #reverse string using slicing
    return word == reverse_word     #returns true if it's equal, otherwise returns false
    
while True:
    user_input = input("Please type in a palindrome: ")
    if palindromes(user_input):
        print(f"{user_input} is a palindrome!")
        break
    print("that wasn't a palindrome")


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":

#     user_input = input("Please type in a palindrome: ")
#     if palindromes(user_input):
#         print(f"{user_input} is a palindrome!")
#     else:
#         print("that wasn't a palindrome")
        