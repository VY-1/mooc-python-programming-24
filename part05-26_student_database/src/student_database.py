# Write your solution here
def add_student(students:dict, name:str):
    students[name] = {}
def print_student(students:dict, name:str):
    if name in students:
        print(f"{name}:")
        if students[name]:
            grades =[]
            print(f" {len(students[name])} completed courses: ")
            for key,value in students[name].items():
                print(f"  {key} {value}")
                grades.append(value)
            print(f" average grade {sum(grades)/len(grades)}")
        else:
            print(f" no completed courses")
    else:
        print(f"{name}: no such person in the database")
        
def add_course(students:dict, name:str, course:tuple):
    # if course grade == 0 return
    if course[1] == 0:
        return
    elif course[0] in students[name]:
        if students[name][course[0]] < course[1]:
            students[name][course[0]] = course[1]
    else:
        new_dict = {}
        new_dict[course[0]] = course[1]
        students[name].update(new_dict)


def summary(students: dict):
    most_courses = 0
    most_courses_name = ''
    best_avg = 0
    best_avg_name = ''
    for student, courses_data in students.items():
        if len(courses_data) > most_courses:
            most_courses = len(courses_data)
            most_courses_name = student
        avg_grade = sum(courses_data.values())/len(courses_data.values())
        if avg_grade > best_avg:
            best_avg = avg_grade
            best_avg_name = student

    print(f'students {len(students)}')
    print(f'most courses completed {most_courses} {most_courses_name}')
    print(f'best average grade {best_avg} {best_avg_name}')
        
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")