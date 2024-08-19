# Write your solution here
eat_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
groceries_spend = float(input("How much money do you spend on groceries in a week? "))

print(f"\nAverage food expenditure:\nDaily: {(eat_per_week*lunch_price+groceries_spend)/7} euros\nWeekly: {eat_per_week*lunch_price + groceries_spend} euros")