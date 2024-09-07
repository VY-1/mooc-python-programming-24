# write your solution here
def read_fruits()->dict:
    new_dict = {}
    with open("src/fruits.csv") as new_file:
        for line in new_file:
            parts = line.split(";")     #split at ";" and store in parts
            key, value = parts[0], float(parts[1])      #convert parts[1] as float and store in value
            new_dict[key] = value       #add key, value to new_dict
    return new_dict

if __name__ == "__main__":
    print(read_fruits())