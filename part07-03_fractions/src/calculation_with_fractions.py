# Write your solution here
import fractions
from fractions import Fraction


def fractionate(amount: int):
    fraction_list =[]
    for _ in range(amount):
        fraction_list.append(Fraction(1, amount))
    return fraction_list

if __name__ == "__main__":

    print(dir(fractions.Fraction))

    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))