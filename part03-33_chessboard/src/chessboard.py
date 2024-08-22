# Write your solution here

def chessboard(length:int):
    first_row = "1"
    second_row = "0"
    
    #creating pattern for first_row
    while len(first_row) < length:
        if first_row[-1] == "1":    # check if the last char is 1, if it is append 0
            first_row += "0"
        else:
            first_row += "1"
    
    #creating pattern for second_row
    while len(second_row) < length:
        if second_row[-1] == "1":
            second_row += "0"
        else:
            second_row += "1"

    #printing rows based on length
    count = 1
    while count <= length:
        if count % 2 != 0:
            print(first_row)
        else:
            print(second_row)
        count += 1
        
# Testing the function
if __name__ == "__main__":
    chessboard(3)
