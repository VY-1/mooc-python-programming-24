# Write your solution here
def row_sums(my_matrix: list):
    for index, matrix in enumerate(my_matrix):
        my_matrix[index].append(sum(matrix))    #modify matrix in place by appending the sum


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)