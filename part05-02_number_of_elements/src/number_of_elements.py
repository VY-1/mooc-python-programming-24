# Write your solution here
def count_matching_elements(my_matrix: list, element: int) -> int:
    match = 0
    for row in my_matrix:
        for item in row:
            if item == element:
                match +=1
    return match

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))