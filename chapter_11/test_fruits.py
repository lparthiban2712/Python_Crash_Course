from fruits import MyFruits
import pytest

@pytest.fixture
def create_fruit_object():
    fruit_obj= MyFruits("Which fruits do you like?")
    return fruit_obj

def test_single_fruit_addition(create_fruit_object):
    create_fruit_object.add_fruit("Apple")
    assert'Apple' in create_fruit_object.fruits

def test_multiple_fruit_addition(create_fruit_object):
    fruits_to_add = ["Banana", "Orange", "Grapes"]
    for fruit in fruits_to_add:
        create_fruit_object.add_fruit(fruit)
    for fruit in fruits_to_add:
        assert fruit in create_fruit_object.fruits