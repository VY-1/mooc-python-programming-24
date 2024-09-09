# write your solution here
student_info = input("Student information: ")
exercise_complete = input("Exercises completed: ")

students = {}
with open(student_info) as student_file:
    for line in student_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        id = parts[0]
        first = parts[1]
        last = parts[2]
        if id == "id":
            continue

        students[id] = f"{first} {last}"

exercises = {}
with open(exercise_complete) as exercise_file:
    for line in exercise_file:
        line = line.replace("\n", "")
        parts = line.split(";")

        id = parts[0]
        if id == "id":
            continue
        e1,e2,e3,e4,e5,e6,e7 = int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6]), int(parts[7])

        #print(f"{id} {sum([e1,e2,e3,e4,e5,e6,e7])}")

        exercises[id] = f"{sum([e1,e2,e3,e4,e5,e6,e7])}"

for id, student in students.items():
    if id in exercises:
        print(student, exercises[id])