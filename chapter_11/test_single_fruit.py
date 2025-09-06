from fruits import MyFruits
def test_single_fruit():
    sf= MyFruits("Which fruit do you like?")
    print(sf.question)
    input_fruit = input("Enter a fruit: ")
    sf.add_fruit(input_fruit)
    assert input_fruit in sf.fruits