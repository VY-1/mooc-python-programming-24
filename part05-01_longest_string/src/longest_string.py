# Write your solution here
def longest(strings: list):
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))