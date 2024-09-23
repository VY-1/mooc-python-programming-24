# Write your solution here
def read_input(prompt:str, low:int, high:int):
    while True:
        user_input = input(prompt)

        try:
            user_input = int(user_input)
        except ValueError:
            user_input = low-1

        if user_input >= low and user_input <=high:
            return user_input

        else:
            print(f"You must type in an integer between {low} and {high}")

if __name__ == "__main__":

    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)