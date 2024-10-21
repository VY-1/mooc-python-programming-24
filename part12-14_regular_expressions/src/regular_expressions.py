# Write your solution here
import re
def is_dotw(my_string: str):
    valid_day = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(valid_day, my_string):
        return True
    else:
        return False

def all_vowels(my_string: str):
    for a in my_string:
        if re.search("[aeiouAEIOU]", a):
            continue
        else:
            return False
    return True

def time_of_day(my_string: str):
    if re.search("^([0-1][0-9]|[2][0-4]):[0-5][0-9]:[0-5][0-9]$", my_string):
        return True
    else:
        return False

if __name__== "__main__":
    print("Days of the week")
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

    print()
    print("Check for vowels")
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

    print()
    print("Time of day")
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))