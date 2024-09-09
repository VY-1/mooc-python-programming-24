# write your solution here
if False:
    student_info = input("Student information: ")
    exercise_complete = input("Exercises completed: ")
    exam_points = inpu("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_complete = "exercises1.csv"
    exam_points = "exam_points1.csv"
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

exams = {}
with open(exam_points) as exam_file:
    for line in exam_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        id = parts[0]
        if id == "id":
            continue
        e1, e2, e3 = int(parts[1]), int(parts[2]), int(parts[3])
        exams[id] = f"{sum([e1,e2,e3])}"

for id, student in students.items():
    grade = int(exams[id]) + int(exercises[id])/40*100//10
    if grade > 28:
        print(student, 5)
    elif grade >= 24:
        print(student, 4)
    elif grade >= 21:
        print(student, 3)
    elif grade >= 18:
        print(student, 2)
    elif grade >=15:
        print(student, 1)
    else:
        print(student, 0)