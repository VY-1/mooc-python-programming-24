# Write your solution here

def squared(text:str, number:int):
    text = text * number * number
    counter = 0
    start = 0
    while counter < number:
        print(text[start:start + number])
        start += number
        counter += 1
        
        
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)