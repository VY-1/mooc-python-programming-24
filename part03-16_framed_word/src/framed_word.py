# Write your solution here
import math

word = input("Word: ")

#seting up padding between word
frame_padding = (28 -len(word))//2
frame_padding = " "*frame_padding

#Display base on word length odd or even
print("*"*30)
if len(word) % 2 !=0:
    print(f"*{frame_padding}{word} {frame_padding}*")
else:
    print(f"*{frame_padding}{word}{frame_padding}*")
print("*"*30)