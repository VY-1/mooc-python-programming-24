# Write your solution here

def transpose(matrix: list):
    new_matrix = []      #copy matirx to new_matrix, deep copy
    for row in matrix:
        new_matrix.append(row[:])   #copy elements in the row
    
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[col][row] = new_matrix[row][col]    
    
    

if __name__ == "__main__":
    
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    
    transpose(matrix)
    
    print(matrix)