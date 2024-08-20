# Write your solution here
point = int(input("How many points [0-100]: "))

if point < 0 or point > 100:
    grade = "impossible!"
    
elif point >= 90:
    grade = 5    
elif point >= 80:
    grade = 4
elif point >= 70:
    grade = 3
elif point >= 60:
    grade = 2
elif point >= 50:
    grade = 1
else:
    grade = "fail"
    
print(f"Grade: {grade}")