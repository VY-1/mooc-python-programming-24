# Write your solution here
def length_of_longest(string_list: list) ->int:
    longest = 0
    for word in string_list:
        if len(word) > longest:
            longest = len(word)
    return longest

#Test code

if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)