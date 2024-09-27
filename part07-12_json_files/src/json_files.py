# Write your solution here
import json

def read_json(json_in: str):
    with open(json_in) as json_file:
        data = json_file.read()
        return data

def print_persons(filename: str):
    data = read_json(filename)
    persons_data = json.loads(data)
    for person in persons_data:
        print(f"{person["name"]} {person["age"]} years ({", ".join(person["hobbies"])})")

if __name__ == "__main__":
    print_persons("file1.json")