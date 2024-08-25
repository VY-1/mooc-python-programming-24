# Write your solution here

my_list = []
user_input = ""
count = 1
while True:
    user_input = input("a(d)d, (r)emove or e(x)it: ")

    if user_input == "d":
        my_list.append(count)
        count += 1
    if user_input == "r":
        my_list.pop()
        count -=1
    if user_input == "x":
        break

    print(my_list)
print("Bye!")