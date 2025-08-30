def my_dog(name, age, color='brown'):
    print(f"\nI have a {color} dog.")
    print(f"My dog's name is {name}.")
    print(f"My dog is {age} years old.")
    print("Woof! Woof!")

my_dog('Willie', 6) # Positional arguments with default color
my_dog('Lucy', 3, 'black') # Positional arguments with specified color

my_dog(age=4, name='Buddy') # Keyword arguments
my_dog(name='Daisy', age=5, color='white') # Keyword arguments with specified color     
my_dog('Max', age=2) # Mixed positional and keyword arguments
my_dog('Charlie', color='golden', age=7) # Mixed positional and keyword arguments
# my_dog(color='gray', 'Rocky', 4) # This will raise a SyntaxError