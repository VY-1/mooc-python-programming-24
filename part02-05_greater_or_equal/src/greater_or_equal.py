# Write your solution here

first_num = int(input("Please type in the first number: "))
second_num = int(input("Please type in another number: "))

if first_num > second_num:
    print(f"The greater number was: {first_num}")
elif first_num < second_num:
    print(f"The greater number was: {second_num}")
else:
    print("The numbers are equal!")