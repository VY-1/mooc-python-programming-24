# Write your solution here!
class  NumberStats():
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if self.count_numbers() == 0:
            return 0
        return sum(self.numbers)

    def average(self):
        if self.count_numbers() == 0:
            return 0
        return sum(self.numbers)/self.count_numbers()

print("Please type in integer numbers:")
stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

while True:
    user_input = int(input(""))
    if user_input == -1:
        break
    if user_input % 2 == 0:
        even_stats.add_number(user_input)
    else:
        odd_stats.add_number(user_input)

    stats.add_number(user_input)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even_stats.get_sum()}")
print(f"Sum of odd numbers: {odd_stats.get_sum()}")