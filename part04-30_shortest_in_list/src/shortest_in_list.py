# Write your solution here

def shortest(string_list:list) -> str:
    shortest = string_list[0]
    for word in string_list:
        if len(word) < len(shortest):
            shortest = word
    return shortest

# Test Code
if __name__ == "__main__":
    
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)