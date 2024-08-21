# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

num_count = 0
sum = 0
mean = 0
neg_num = 0
pos_num = 0
while True:
    number = int(input("Number: "))
    
    if number == 0:
        break
    if number < 0:
        neg_num +=1
    else:
        pos_num +=1
        
    num_count +=1
    sum += number
    mean = sum/num_count
    

    
print(f"Numbers typed in {num_count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos_num}")
print(f"Negative numbers {neg_num}")