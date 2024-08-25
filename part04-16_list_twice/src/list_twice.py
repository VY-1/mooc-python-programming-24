# Write your solution here


items_list = []

while True:
    
    new_item = int(input("New item: "))
    
    if new_item == 0:
        break
    
    items_list.append(new_item)
    print(f"The list now: {items_list}")
    print(f"The list in order: {sorted(items_list)}")
    
print("Bye!")