# Write your solution here
import math
number_of_student = int(input("How many students on the course? "))
group_size = int(input("Desire group size? "))
print(f"Number of groups formed: {math.ceil(number_of_student/group_size)}")