# Write your solution here

user_input = int(input("Please type in a positive integer: "))

for i in range(-user_input, user_input+1):
    #continue with the loop if i == 0
    if i == 0:
        continue
    
    print(i)
    