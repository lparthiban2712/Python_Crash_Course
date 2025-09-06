class MyFruits:
    def __init__(self, question):
        self.question = question
        self.fruits = []
    
    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def display_fruits(self):
        for fruit in self.fruits:
            print(fruit)