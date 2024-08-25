# Write your solution here
def same_chars(word:str, num1:int, num2:int):
    if (num1 >= len(word) or (num2 >= len(word))):
        return False
    if word[num1] == word[num2]:
        return True
    else:
        return False
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("coder",1, 10))