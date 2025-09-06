from fruits import MyFruits
def test_multiple_fruits():
    mf = MyFruits("Which fruits do you like?")
    print(mf.question)
    while True:
        input_fruit = input("Enter a fruit (or 'q' to quit): ")
        if input_fruit.lower() == 'q':
            break
        mf.add_fruit(input_fruit)
    for fruit in mf.fruits:
        assert fruit in mf.fruits