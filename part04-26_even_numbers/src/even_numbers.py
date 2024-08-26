# Write your solution here

def even_numbers(my_list:list) -> list:
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


# Test Code
if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)