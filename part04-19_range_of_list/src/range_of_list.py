# Write your solution here

def range_of_list(my_int_list: list) -> int:
    smallest = min(my_int_list)     #get the smallest num
    largest = max(my_int_list)      #get the largest num
    return largest - smallest       #return the difference

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)