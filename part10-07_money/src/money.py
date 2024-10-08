# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    # @property
    # def euros(self):
    #     return self.__euros

    # @property
    # def cents(self):
    #     return self.__cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        if self.__euros == another.__euros and self.__cents == another.__cents:
            return True
        return False

    def __lt__(self, another):
        if self.__euros + self.__cents/100 < another.__euros + another.__cents/100:
            return True
        return False

    def __gt__(self, another):
        if self.__euros + self.__cents/100 > another.__euros + another.__cents/100:
            return True
        return False

    def __ne__(self, another):
        if self.__euros + self.__cents/100 != another.__euros + another.__cents/100:
            return True
        return False

    def __add__(self, another):
        total_euros = self.__euros + another.__euros
        total_cents = self.__cents + another.__cents
        if self.__euros < 0 or self.__cents < 0 or another.__euros <0 or another.__cents <0:
            raise ValueError("a nagative result is not allowed")

        if total_cents > 99:
            cent_remain = total_cents % 100
            cent_to_euro = total_cents // 100
            total_euros += cent_to_euro
            total_cents = cent_remain

        new_value = Money(total_euros, total_cents)
        return new_value

    def __sub__(self, another):

        if self.__euros < 0 or self.__cents < 0 or another.__euros <0 or another.__cents <0:
            raise ValueError("a nagative result is not allowed")

        if another > self:
            raise ValueError("a nagative result is not allowed")
        total_euros = self.__euros - another.__euros
        total_cents = self.__cents - another.__cents
        if total_cents < 0:
            total_euros -=1
            total_cents = 100 + total_cents

        new_value = Money(total_euros, total_cents)
        return new_value

if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents

    print(e1)
    print(e2)

    print()

    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)

    print()

    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

    print()

    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2 - e1