# Write your solution here
def factorials(n: int) -> dict:
    new_dict = {}
    result = 1
    for value in range(1, n+1):
        result *=value
        new_dict[value] = result

    return new_dict

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])