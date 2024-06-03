import random
import pytest
import add_path
from mit_ocw_data_science.lec2.menu import *


def test_menu():
    names = ["apple", "banana", "orange"]
    values = [10, 20, 30]
    calories = [50, 100, 150]
    expected_foods = [
        Food("apple", 10, 50),
        Food("banana", 20, 100),
        Food("orange", 30, 150),
    ]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    print(menu)

    assert foods[0].get_cost() == expected_foods[0].get_cost()
    assert foods[1].get_value() == expected_foods[1].get_value()
    assert Menu.get_foods_str(foods) == \
        'apple: <10, 50>; banana: <20, 100>; orange: <30, 150>; '

def test_6_menu():
    names = ["Calculus","Physics","OOP", "Wine", "Beer", "Whiskey"]
    values = [50, 60, 30, 20, 10, 100]
    calories = [100, 200, 150, 80, 20, 500]
    expected_foods = [
        Food("Calculus", 50, 100),
        Food("Physics", 60, 200),
        Food("OOP", 30, 150),
        Food("Wine", 20, 80),
        Food("Beer", 10, 20),
        Food("Whiskey", 100, 500),
    ]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    print(menu)

    assert foods[0].get_cost() == expected_foods[0].get_cost()
    assert foods[1].get_value() == expected_foods[1].get_value()
    assert Menu.get_foods_str(foods) == \
        'Calculus: <50, 100>; Physics: <60, 200>; OOP: <30, 150>; Wine: <20, 80>; Beer: <10, 20>; Whiskey: <100, 500>; '

def test_build_large_menu():
    menu = Menu()
    num_items = 10
    max_val = 50
    max_cost = 400
    menu.build_large_menu(num_items, max_val, max_cost)
    foods = menu.get_foods()

    print(menu)
    assert len(foods) == num_items
    if num_items > 0:
        assert foods[0].get_value() <= max_val
        assert foods[0].get_cost() <= max_cost

