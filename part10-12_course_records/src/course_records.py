# tee ratkaisusi tänne

class Course:
    def __init__(self, name: str, grade: int, credits: int ):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def __str__(self):
        return f"{self.name()} ({self.__credits} cr) grade {self.grade()}"

class Statistics:
    def __init__(self):
        self.__courses = {}


    # Add course if it doesn't exist or update course to batter grades
    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.__courses:      #if course doesn't exist add it
            self.__courses[name] = Course(name, grade, credits)
        course = self.__courses[name]
        if course.grade() < grade:      #if grade is higher than existing grade, update
            self.__courses[name] = Course(name, grade, credits)

    def get_course_data(self, name: str):
        if name not in self.__courses:
            return "no entry for this course"
        return self.__courses[name]

    def __get_distribution(self):
        grade_distribution = {5: "", 4: "", 3: "", 2: "", 1: ""}
        for course, value in self.__courses.items():
            grade_distribution[value.grade()] += "x"
        return grade_distribution

    def stats(self):
        total_credits = 0
        total_grade = 0
        mean = 0
        for course, value in self.__courses.items():
            total_credits += value.credits()
            total_grade += value.grade()
        mean = round(total_grade/len(self.__courses), 1)        #round decimal point to 1 digit
        print(f"{len(self.__courses)} completed courses, a total of {total_credits} credits")
        print(f"mean {mean}")
        print("grade distribution")
        for grade, distribution in self.__get_distribution().items():
            print(f"{grade}: {distribution}")

class CourseStatsApplication:
    def __init__(self):
        self.__course_stats = Statistics()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__course_stats.add_course(name, grade, credits)

    def get_course(self):
        name = input("course: ")
        course = self.__course_stats.get_course_data(name)
        print(course)
    def get_stats(self):
        self.__course_stats.stats()

    def execute(self):
        self.help()
        while True:
            print()
            command = input("Command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course()
            elif command == "3":
                self.get_stats()

            else:
                self.help()


application = CourseStatsApplication()
application.execute()