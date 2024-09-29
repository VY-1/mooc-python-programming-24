# Write your solution here
import csv
from datetime import datetime, time, timedelta


def read_csv(file_in: str):
    with open(file_in) as csv_file:
        time_list = []
        for line in csv.reader(csv_file, delimiter=";"):
            time_list.append(line)

        return time_list

def cheaters():
    start_time_list = read_csv("start_times.csv")
    submission_time_list = read_csv("submissions.csv")
    cheaters_list = []
    for submission in submission_time_list:
        student_name = submission[0]
        submission_time = datetime.strptime(submission[3], "%H:%M")

        print(submission_time)
        for line in start_time_list:
            start_time = datetime.strptime(line[1], "%H:%M")
            if student_name in line[0]:
                if submission_time > (start_time + timedelta(hours=3)) and student_name not in cheaters_list:
                    cheaters_list.append(student_name)

    return cheaters_list

if __name__ == "__main__":
    start_time_list = read_csv("start_times.csv")
    submission_time_list = read_csv("submissions.csv")
    my_time = "12:18"
    print(datetime.strptime(my_time, "%H:%M").time())

    print()
    print(cheaters())