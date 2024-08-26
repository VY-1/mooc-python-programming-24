# Write your solution here
def most_common_character(string:str):
    most_common = string[0]
    for ch in string:
        if string.count(ch) > string.count(most_common):
            most_common = ch
    return most_common

#Test Code
if __name__ == "__main__":
    
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))