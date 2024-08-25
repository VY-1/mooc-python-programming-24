# Write your solution here

word_list = []

while True:
    
    word = input("Word: ")
    if word in word_list:
        break
    word_list.append(word)

print(f"You typed in {len(word_list)} different words")
        