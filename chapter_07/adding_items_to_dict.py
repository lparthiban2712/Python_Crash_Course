responses={}

while True:
    name=input("Enter your name")
    response=input("Enter the mountains you like")
    responses[name]=response
    repeat=input("Would you like to let another person respond? (yes/no) ")

    if repeat.lower()=='yes':
        break
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")