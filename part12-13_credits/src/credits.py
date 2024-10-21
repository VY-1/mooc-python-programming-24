from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda reduced_sum, item: reduced_sum + item.credits, attempts,0)

def sum_of_passed_credits(attempts: list):
    passing = list(filter(lambda attempt: attempt.grade >=1, attempts))

    return reduce(lambda sum, attempt_pass: sum + attempt_pass.credits, passing, 0)

def average(attempts: list):
    passing = list(filter(lambda attempt: attempt.grade >= 1, attempts))

    total_passing_grade = reduce(lambda sum, attempt_pass: sum + attempt_pass.grade, passing, 0)
    return total_passing_grade/len(passing)

if __name__=="__main__":
    attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)
    print(attempt)
    print(attempt.course_name)
    print(attempt.credits)
    print(attempt.grade)

    print()
    print("The sum of all credits")
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    print()
    print("The sum of passed credits")
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    print()
    print("Average grade for passed courses")
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)