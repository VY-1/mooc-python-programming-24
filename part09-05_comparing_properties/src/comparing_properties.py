# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm


    def bigger(self, compared_to)-> bool:
        if self.square_metres > compared_to.square_metres:
            return True
        return False

    def price_difference(self, compare_to)-> int:
        difference = abs(self.price_per_sqm * self.square_metres - compare_to.price_per_sqm * compare_to.square_metres)
        return difference

    def more_expensive(self, compare_to)-> bool:
        if self.price_per_sqm * self.square_metres > compare_to.price_per_sqm * compare_to.square_metres:
            return True
        return False

if __name__ == "__main__":
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.bigger(downtown_two_bedroom))
    print(suburbs_three_bedroom.bigger(downtown_two_bedroom))

    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.price_difference(downtown_two_bedroom))
    print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))

    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.more_expensive(downtown_two_bedroom))
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))