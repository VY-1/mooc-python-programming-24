# Write your solution here
def remove_smallest(numbers:list):
    smallest = numbers[0]       #assign the first index as smallest
    for item in numbers:
        if item < smallest:     #if anyitem on the list smaller than first index, set it as smallest
            smallest = item

    numbers.remove(smallest)    #remove the smallest value from list

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)