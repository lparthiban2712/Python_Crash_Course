numbers = [1, 2, 3, 4, 5]
i=-1
while numbers:
    i+=1
    current_number = numbers[i]
    if current_number == 2:
        continue
    if current_number == 5:
        break
    print(current_number)
    