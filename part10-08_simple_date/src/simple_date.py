# WRITE YOUR SOLUTION HERE:

# class SimpleDate:
#     def __init__(self, day: int, month: int, year: int):
#         self.__day = day
#         self.__month = month
#         self.__year = year

#     def __eq__(self, another):
#         if self.__day == another.__day and self.__month == another.__month and self.__year == another.__year:
#             return True
#         return False

#     def __ne__(self, another):
#         if self.__eq__(another) == False:
#             return True
#         return False

#     def __str__(self):
#         return f"{self.__day}.{self.__month}.{self.__year}"

#     def __lt__(self, another):
#         if self.__year < another.__year:
#             return True
#         elif self.__year == another.__year:
#             if self.__month < another.__month:
#                 return True
#             elif self.__month == another.__month:
#                 return self.__day < another.__day
#         return False

#     def __gt__(self, another):
#         if self.__lt__(another) == False and self != another:
#             return True
#         return False

#     def __convert_date_to_days(self):
#         days = ((self.__year - 1) * 12 * 30) + ((self.__month - 1) * 30) + self.__day
#         return days

#     def __add__(self, days_to_add: int):
#         days = self.__convert_date_to_days()
#         days += days_to_add
#         year = (days // 360) + 1
#         month = ((days // 30) % 12) + 1
#         day = days % 30
#         return SimpleDate(day, month, year)

#     def __sub__(self, another):
#         curr_days = self.__convert_date_to_days()
#         another_days = another.__convert_date_to_days()
#         return abs(curr_days - another_days)


class SimpleDate:
    def __init__(self, pv: int, month: int, year: int):
        self.__pv = pv
        self.__month = month
        self.__year = year
 
    def __str__(self):
        return f'{self.__pv}.{self.__month}.{self.__year}'
 
    # Comparisons are easier, when date is converted to days
    def __value(self):
        return self.__year * 360 + self.__month * 30 + self.__pv
 
    # Converst days back to date
    def __to_date(self, days: int):
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)
 
    def __lt__(self, other: "SimpleDate"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "SimpleDate"):
        return self.__value() > other.__value()
 
    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()
        
    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()
 
    def __add__(self, days_to_add: int):
        return self.__to_date(self.__value() + days_to_add)
 
    def __sub__(self, other: "SimpleDate"):
        # abs(x) returns the absolute value of x
        return abs(self.__value() - other.__value())


if __name__ == "__main__":

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)

    print()

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)

    print()

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)