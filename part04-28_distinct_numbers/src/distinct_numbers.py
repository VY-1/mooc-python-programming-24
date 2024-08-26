# Write your solution here
def distinct_numbers(my_list:list) -> list:
    new_list = []
    for num in my_list:
        if num not in new_list:         # add number if they are not in new_list
            new_list.append(num)
    
    return sorted(new_list)

# Test code
if __name__ == "__main__":
    
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]