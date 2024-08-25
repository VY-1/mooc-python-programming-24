# Write your solution here

user_input = int(input("How many items: "))
my_items = []
count = 1
while count <= user_input:
    
    item = int(input(f"Item {count}: "))
    my_items.append(item)
    count+=1
    
print(my_items)
    
    