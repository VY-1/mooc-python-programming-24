# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_complete = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "src/students1.csv"
    exercise_complete = "src/exercises1.csv"
    exam_points = "src/exam_points1.csv"

def string_to_int(input_dict: dict) -> dict:
    new_dict = {}
    for key, value in input_dict.items():
        for index, list_value in enumerate(value):
            value[index] = int(list_value)
        new_dict[key] = value
    return new_dict

def points_to_grade(grade):
    if grade > 28:
        return 5
    elif grade >= 24:
        return 4
    elif grade >= 21:
        return 3
    elif grade >= 18:
        return 2
    elif grade >= 15:
        return 1
    else:
        return 0
    
#Refactor read files
def read_file(file_input) ->dict:
    with open(file_input) as new_file:
        new_dict = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            id = parts[0]
            if id == "id":
                continue
            new_dict[id] = parts[1:]
        return new_dict
    
def print_stats(students, exercises, exams):
    label_name = "name"
    exec_nbr = "exec_nbr"
    exec_pts = "exec_pts."
    exm_pts = "exm_pts."
    tot_pts = "tot_pts."
    grade = "grade"

    print(f"{label_name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade:10}")
    for id, name in students.items():
        exercise_total = sum(exercises[id])
        exercise_points = int(((exercise_total/40)*100)//10)
        exam_points = sum(exams[id])
        total_points = exercise_points+exam_points
        grade = points_to_grade(total_points)
        full_name = name[0] + " " + name[1]
        print(f"{full_name:30}{exercise_total:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")


##
students = read_file(student_info)
exercises = string_to_int(read_file(exercise_complete))
exams = string_to_int(read_file(exam_points))

print_stats(students, exercises, exams)
