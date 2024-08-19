# Write your solution here

hr_wage = float(input("Hourly wage: "))
hr_worked = int(input("Hours worked: "))
day_of_week = input("Day of the week: ")
if day_of_week == 'Sunday':
    hr_wage = hr_wage*2
    
print(f"Daily wages: {hr_wage*hr_worked} euros")