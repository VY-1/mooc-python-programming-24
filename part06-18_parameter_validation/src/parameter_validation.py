# Write your solution here
def new_person(name: str, age: int):
    person = tuple()

    if name == "" or len(name.split(" ")) < 2 or len(name) > 40 or age< 0 or age > 150:
        raise ValueError("Invalid parameters")

    person = (name, age)
    return person

if __name__ == "__main__":

    person1 = new_person("Don", 32)
    person2 = new_person("Don Julio", 33)