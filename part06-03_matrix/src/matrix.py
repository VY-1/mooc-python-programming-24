# write your solution here
def matrix_sum()-> int:
    with open("src/matrix.txt") as new_file:
        total = 0
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            for num in numbers:
                total +=int(num)
        return total

def matrix_max() -> int:
    with open("src/matrix.txt") as file:
        file_max = 0
        for line in file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            nums = []
            for num in numbers:
                nums.append(int(num))
            if max(nums) > file_max:
                file_max = max(nums)
        return file_max


def row_sums() -> list:
    with open("src/matrix.txt") as file:
        file_row_sums = []
        for line in file:
            line = line.replace("\n","")
            numbers = line.split(",")
            nums = []
            for num in numbers:
                nums.append(int(num))
            file_row_sums.append(sum(nums))
        return file_row_sums

if __name__ =="__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())