# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"

class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def items(self):
        return self.__items

    def weight(self)-> int:
        weights = 0
        for item in self.items():
            weights += item.weight()
        return weights

    def print_items(self):
        for item in self.items():
            print(item)

    def heaviest_item(self)-> Item:
        if not self.items():        #check if empty, returns none
            return None

        heaviest = self.items()[0]
        for item in self.items():
            if item.weight() >= heaviest.weight():
                heaviest = item
        return heaviest

    def __str__(self):
        if len(self.items()) == 1:
            return f"{len(self.items())} item ({self.weight()} kg)"
        return f"{len(self.items())} items ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def suitcases(self):
        return self.__suitcases

    def weight(self):
        weight = 0
        for suitcase in self.suitcases():
            weight += suitcase.weight()
        return weight

    def print_items(self):
        for suitcase in self.suitcases():
            suitcase.print_items()

    def __str__(self):
        if len(self.suitcases()) == 1:
            return f"{len(self.suitcases())} suitcase, space for {self.__max_weight - self.weight()} kg"
        return f"{len(self.suitcases())} suitcases, space for {self.__max_weight - self.weight()} kg"

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()