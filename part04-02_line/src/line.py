# Write your solution here

def line(number:int, text:str):
    if text == "":
        text = "*"
    print(text[0]*number)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")