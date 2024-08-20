from math import sqrt
# Write your solution here

while True:
    
    number = int(input("Please type in a number: "))
    #Checking edge cases
    if number == 0:
        break
    
    if number < 0:
        print("Invalid number")
    else:
        print(f"{sqrt(number)}")
        
print("Exiting...")