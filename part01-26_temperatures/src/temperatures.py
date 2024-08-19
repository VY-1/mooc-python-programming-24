# Write your solution here
temp_in_fahrenheit = float(input("Please type in a temperature (F): "))
celsius = (temp_in_fahrenheit-32)*5/9
print(f"{temp_in_fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")