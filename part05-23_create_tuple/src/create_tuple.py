# Write your solution here
def create_tuple(x:int, y:int, z:int) -> tuple:

    smallest = min(x,y,z)
    largest = max(x,y,z)
    total = sum([x,y,z])    #use sum to total up element in list
    my_tuple = (smallest, largest, total)
    return my_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))