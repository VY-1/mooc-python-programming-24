# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    number_list = list(range(lower, upper))
    pick_amount = sample(number_list, amount)
    pick_amount.sort()
    return pick_amount

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)

