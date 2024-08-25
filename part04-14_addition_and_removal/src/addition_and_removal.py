# Write your solution here

my_list = []
count = 1
while True:
    print(f"The list is now {my_list}")

    user_input = input("a(d)d, (r)emove or e(x)it: ")

    if user_input == "d":
        my_list.append(count)
        count += 1
    if user_input == "r" and len(my_list)>0:
        my_list.pop()
        count -=1
    if user_input == "x":
        break

print("Bye!")