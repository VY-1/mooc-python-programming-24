# Write your solution here



while True:
    number = int(input("Please type in a number: "))
    count = 1
    factorial = 1
    
    if number <= 0:
        break
    
    while count <= number:
        factorial *= count
        count += 1
    
    print(f"The factorial of the number {number} is {factorial}")

print("Thanks and bye!")