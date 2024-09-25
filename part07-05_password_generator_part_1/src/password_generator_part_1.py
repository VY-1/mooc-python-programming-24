# Write your solution here
from random import choice
def generate_password(lenght: int):
    characters = "abcdefghijklmnopqrstuvwxyz"
    password =""
    for _ in range(lenght):
        password +=choice(characters)
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))