# Write your solution here
def write_file(file_out, person:tuple):
    with open(file_out, "a") as new_file:
        new_file.write(f"{person[0]};{int(person[1])};{float(person[2])}\n")

def store_personal_data(person:tuple):
    write_file("people.csv", person)

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
    store_personal_data(("Dave Paulson", 24, 139.3))