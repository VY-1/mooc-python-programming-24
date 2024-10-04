# WRITE YOUR SOLUTION HERE:
from random import shuffle


class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
        self.total_height = 0


    def add(self, person):
        self.persons.append(person)
        self.total_height += person.height

    def is_empty(self)-> bool:
        if not self.persons:
            return True
        return False

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.total_height} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self)-> Person:
        if self.is_empty():
            return None
        shortest_person = self.persons[0]
        for person in self.persons:
            if person.height < shortest_person.height:
                shortest_person = person
        return shortest_person

    def remove_shortest(self)-> Person:
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)
        return shortest_person

if __name__ == "__main__":
    room = Room()
    print(room.is_empty())
    room.add(Person("Joe", 5.11))
    print(room.is_empty())

    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()

    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()

    room = Room()
    print(room.remove_shortest())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()