# Write your solution here

def list_sum(list1:list, list2:list) -> list:
    new_list = []
    if len(list1) == len(list2):
        for num1, num2 in zip(list1,list2):    # iterate 2 lists and add each value in index
            new_list.append(num1+num2)
    
    return new_list

# Alternate method
# def list_sum(list1: list, list2: list):
#     results = []
#     for i in range(len(list1)):
#         results.append(list1[i] + list2[i])

# Test Code
if __name__ == "__main__":

    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]