# Write your solution here
value_of_gift = int(input("Value of gift: "))
tax = 0

if value_of_gift < 5000:
    tax = 0

elif value_of_gift >=5000 and value_of_gift <=25000:
    tax = float(100+(value_of_gift-5000)*0.08)
elif value_of_gift >25000 and value_of_gift<=55000:
    tax = float(1700+(value_of_gift-25000)*0.10)
elif value_of_gift >55000 and value_of_gift<=200000:
    tax = float(4700+(value_of_gift-55000)*0.12)
elif value_of_gift >200000 and value_of_gift<=1000000:
    tax = float(22100+(value_of_gift-200000)*0.15)
else:
    tax = float(142100+(value_of_gift-1000000)*0.17)

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")