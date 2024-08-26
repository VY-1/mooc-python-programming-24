# Write your solution here
def formatted(my_float_list:list) ->list:
    new_list = []
    for num in my_float_list:
        new_list.append(f"{num:.2f}")
    return new_list

#Test code
if __name__ == "__main__":
        
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)