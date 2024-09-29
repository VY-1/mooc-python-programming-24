# Write your solution here
import math
import urllib.request
import json


def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    request = urllib.request.urlopen(address)
    data = request.read()
    json_data = json.loads(data)

    active_course = []

    for line in json_data:
        if line["enabled"]:     #if enable is true, get info and store in variables
            full_name = line["fullName"]
            name = line["name"]
            year = line["year"]
            exercises = sum(line["exercises"])      #sum the values in the list of exercises
            course = (full_name, name, year, exercises)     #add course info into tuple

            active_course.append(course)        # add tuple to active_course list

    return active_course

def retrieve_course(course_name: str):
    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    request = urllib.request.urlopen(address)
    data = request.read()
    json_data = json.loads(data)

    weeks = len(json_data)
    students = 0
    hours = 0
    hours_average = 0
    exercises = 0
    exercises_average = 0
    for key, value in json_data.items():
        
        if value["students"] > students:
            students = value["students"]

        hours += value["hour_total"]
        exercises += value["exercise_total"]
    hours_average = math.floor(hours/students)
    exercises_average = math.floor(exercises/students)

    course_data = {}
    course_data["weeks"] = weeks
    course_data["students"] = students
    course_data["hours"] = hours
    course_data["hours_average"] = hours_average
    course_data["exercises"] = exercises
    course_data["exercises_average"] = exercises_average


    return course_data

if __name__ == "__main__":
    print(retrieve_all())

    retrieve_course("docker2019")