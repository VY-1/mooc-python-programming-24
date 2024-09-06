# Write your solution here

layer = int(input("Layers: "))

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

left = ""  # section, that goes downwards
right = ""  # section, that goes upwards
k = layer - 1  #location of the next char
m = 2 * layer - 1  # the number of characters between
while k >= 1:
    left = left + alphabets[k]
    right = alphabets[k] + right
    m -= 2
    print(left + alphabets[k] * m + right)
    k -= 1
while k <= layer - 1:
    print(left + alphabets[k] * m + right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1