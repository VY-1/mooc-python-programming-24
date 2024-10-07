# WRITE YOUR SOLUTION HERE:
from collections import Counter

class ListHelper:
 
    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list:
            return None
 
        max_frequency = 0
        max_item = None
        for item in my_list:
            frequency = my_list.count(item)
            if not max_item or frequency > max_frequency:
                max_frequency = frequency
                max_item = item
 
        return max_item
 
    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)
 
        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1
 
        return doubles

# class ListHelper:
#     def __init__(self):
#         self.__numbers = []
#     @classmethod
#     def greatest_frequency(cls, my_list: list):
#         frequency = Counter(my_list).most_common(1)
#         return frequency[0][0]

#     @classmethod
#     def doubles(cls, my_list: list):
#         frequency = Counter(my_list)
#         count_keys = sum(1 for value in frequency.values() if value >= 2)
#         return count_keys

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))