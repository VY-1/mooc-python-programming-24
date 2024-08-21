# Write your solution here

#Building String
limit = int(input("Limit: "))
sum_string = ""
sum = 0
count = 1

while sum < limit:
    sum += count
    
    if sum < limit:
        sum_string += f"{count} + "
    else:
        sum_string += f"{count} = "
    
    count+=1
    
print(f"The consecutive sum: {sum_string}{sum}")