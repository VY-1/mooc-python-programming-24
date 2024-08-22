# Write your solution here
def hash_square(length:int):
    hash = "#"
    count = 1
    while count <= length:
        print(hash*length)
        count +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)