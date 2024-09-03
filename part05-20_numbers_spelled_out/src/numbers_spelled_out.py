# Write your solution here

def dict_of_numbers() -> dict:
    new_dict = {}
    zero_to_ten = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    tens_list = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens_list = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    for number in range(100):
        if number < 11:
            new_dict[number] = zero_to_ten[number]
        elif number % 10 == 0:  # check if for tens
            new_dict[number] = tens_list[number//10 - 1]
        elif number < 20:
            new_dict[number] = teens_list[number - 11]
        else:
            tens = number // 10
            unit = number - (tens * 10)
            new_dict[number] = f"{tens_list[tens-1]}-{zero_to_ten[unit]}"
            
    return new_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])