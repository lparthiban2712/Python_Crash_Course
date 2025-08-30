def user_info(name, age):
    print(f"User Name: {name}")
    print(f"User Age: {age}")

user_info("Alice", 30)
user_info("Bob", 25)

def formatted_name(first, last, middle=""):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

print(formatted_name("john", "doe"))
print(formatted_name("john", "doe", "michael"))

def myname(first, last):
    full_name = f"{first} {last}"
    return full_name.title()
print(myname(first="john", last="doe"))
print(myname(last="john", first="doe"))
    