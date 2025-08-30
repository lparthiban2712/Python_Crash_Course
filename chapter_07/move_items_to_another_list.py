fruits=["apple","banana","cherry"]
print("Original list:",fruits)
moved_fruits=[]
while fruits:
    current_fruit=fruits.pop()
    print("Moving fruit:",current_fruit)
    moved_fruits.append(current_fruit)
print("Fruits moved to new list:",moved_fruits)