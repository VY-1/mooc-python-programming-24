# Write your solution here

number = int(input("Please type in a number: "))

count = 1

while count <= number:
    if count + 1 <= number:
        print(count + 1)
    print(count)
    count +=2
   
    
# Alternative    
# number = int(input("Please type in a number: "))
 
# index = 1
# while index+1 <= number:
#     print(index+1)
#     print(index)
#     index += 2
 
# if index <= number:
#     print(index)
 