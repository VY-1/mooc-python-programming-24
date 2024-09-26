# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    numbers = pic[:6]+pic[7:10]
    for x in numbers:
        if x not in "0123456789":
            return False
    century_marker = pic[6]
    if century_marker not in "+-A":
        return False
    day = int(pic[:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    if century_marker == "+":
        year += 1800
    if century_marker == "-":
        year += 1900
    if century_marker == "A":
        year += 2000
    try:
        test = datetime(year, month, day)
    except:
        return False
    characters = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
    index = int(numbers)%31
    return characters[index] == pic[-1]
    
    if __name__ == "__main__":
        print(is_it_valid("230827-906F"))
        print(is_it_valid("120488+246L"))