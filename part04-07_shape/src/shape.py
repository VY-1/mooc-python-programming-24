# Copy here code of line function from previous exercise and use it in your solution

def line(count, character):
    print(character*count)
    
def shape(size, character, height, char2):
    count = 1
    while count <= size:
        line(count, character)
        count+=1
    
    while height > 0:
        line(size, char2)
        height -=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")