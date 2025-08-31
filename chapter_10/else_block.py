from pathlib import Path

while True:
    first_number = input("\nEnter the first number (or 'q' to quit): ")
    if first_number.lower() == 'q':
        break
    second_number = input("Enter the second number (or 'q' to quit): ")
    if second_number.lower() == 'q':
        break
    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
    else:
        print(f"{first_number} divided by {second_number} is {result}") 
        