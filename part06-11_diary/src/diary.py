# Write your solution here

def add_entry(file_input: str, diary_entry: str):
    with open(file_input, "a") as new_file:
        new_file.write(f"{diary_entry}\n")
def read_entry(file_input: str):
    with open(file_input) as new_file:
        print("Entries:")
        for line in new_file:
            line = line.replace("\n", "")
            print(line)

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))

    if function == 0:
        break
    if function == 1:
        diary_entry = input("Diary entry: ")
        add_entry("diary.txt", diary_entry)
        print("Diary saved")
    if function == 2:
        read_entry("diary.txt")
print("Bye now!")