# Write your solution here
def everything_reversed(my_list:list) ->list:
    reverse_list = my_list[::-1]
    everything_reversed = []
    for item in reverse_list:
        everything_reversed.append(item[::-1])
        
    return everything_reversed
    
# Test Code

if __name__ == "__main__":
    
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)