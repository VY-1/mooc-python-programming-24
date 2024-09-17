# Write your solution here
def write_file(file_out:str, line:str):
    with open(file_out, "a") as new_file:
        new_file.write(f"{line}\n")


def filter_solutions():
    open("correct.csv","w").close()
    open("incorrect.csv", "w").close()

    with open("solutions.csv") as file_in:
        for line in file_in:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            problem = parts[1]

            result = parts[2]

            if eval(problem) == int(result):

                write_file("correct.csv", line)
            else:
                write_file("incorrect.csv", line)

if __name__ == "__main__":
    filter_solutions()