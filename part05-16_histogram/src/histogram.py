# Write your solution here
def histogram(word:str):
    new_dict = {}
    for char in word:
        if char not in new_dict:
            new_dict[char] = 0
        new_dict[char] +=1

    for key, value in new_dict.items():
        print(f"{key} {'*'*value}")


if __name__ == "__main__":
    histogram("statistically")