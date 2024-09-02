# Write your solution here
phone_book = {}

while True:
    user_input = int(input("command (1 search, 2 add, 3 quit): "))

    if user_input == 3:
        break
    if user_input == 1:
        name = input("name: ")
        if name in phone_book:
            for value in phone_book[name]:
                print(value)
        else:
            print("no number")
    if user_input == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in phone_book:
            phone_book[name] = [number]
        else:
            phone_book[name].append(number)
        print("ok!")
print("quitting...")