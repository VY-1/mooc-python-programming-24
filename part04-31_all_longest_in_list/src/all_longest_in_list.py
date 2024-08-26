# Write your solution here
#Alternative
# def all_the_longest(string_list:list) -> list:
#     longest = 0
#     longest_list = []
#     for word in string_list:
#         if len(word) > longest:
#             longest = len(word)
            
#     for word in string_list:
#         if len(word) == longest:
#             longest_list.append(word)
#     return longest_list

def all_the_longest(names: list):
    result = []
 
    for name in names:
        if result == [] or len(name) > len(result[0]):
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
 
    return result

# Test code
if __name__ == "__main__":
    
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']