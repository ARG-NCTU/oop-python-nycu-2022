import random
import pytest
import add_path
from mit_ocw_data_science.lec2.menu import *

def test_greedy():
    items = [
        Food("apple", 10, 50),
        Food("banana", 20, 100),
        Food("orange", 30, 150),
    ]
    constraint = 50
    key_function = lambda x: 1 / Food.get_cost(x)

    taken, val = greedy(items, constraint, key_function)
    
    print('Total value of items taken =', val)
    print(Menu.get_foods_str(taken))

    assert val == 10
    assert Menu.get_foods_str(taken) == "apple: <10, 50>; "

def test_greedys():

    names = ['wine', 'beer', 'pizza', 'burger', 'fries',
             'cola', 'apple', 'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    max_units = 750

    print('Use greedy by value to allocate', max_units,
          'calories')
    taken, val = greedy(foods, max_units, Food.get_value)
    expected_str = Menu.get_foods_str(taken)
    assert val == 284 
    assert expected_str == "burger: <100, 354>; pizza: <95, 258>; wine: <89, 123>; "

    print('\nUse greedy by cost to allocate', max_units,
          'calories')
    taken, val = greedy(foods, max_units,
               lambda x: 1/Food.get_cost(x))
    expected_str = Menu.get_foods_str(taken)
    assert val == 318 
    assert expected_str == \
        "apple: <50, 95>; wine: <89, 123>; cola: <79, 150>; beer: <90, 154>; donut: <10, 195>; "
    
    print('\nUse greedy by density to allocate', max_units,
          'calories')
    taken, val = greedy(foods, max_units, Food.density)
    expected_str = Menu.get_foods_str(taken)
    assert val == 318 
    assert expected_str == \
        "wine: <89, 123>; beer: <90, 154>; cola: <79, 150>; apple: <50, 95>; donut: <10, 195>; "

def test_1_greedys():

    name = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'hotdog']
    values = [89, 90, 95, 100, 90, 79, 50, 10, 20]
    calories = [123, 154, 258, 354, 365, 150, 95, 195, 200]
    menu = Menu(name, values, calories)
    foods = menu.get_foods()

    max_units = 750

    print('Use greedy by value to allocate', max_units, 'calories')
    taken, val = greedy(foods, max_units, Food.get_value)
    expected_str = Menu.get_foods_str(taken)
    assert val == 284
    assert expected_str == "burger: <100, 354>; pizza: <95, 258>; wine: <89, 123>; "

    print('\nUse greedy by cost to allocate', max_units, 'calories')
    taken, val = greedy(foods, max_units, lambda x: 1/Food.get_cost(x))
    expected_str = Menu.get_foods_str(taken)
    assert val == 318
    assert expected_str == "apple: <50, 95>; wine: <89, 123>; cola: <79, 150>; beer: <90, 154>; donut: <10, 195>; "

    print('\nUse greedy by density to allocate', max_units, 'calories')
    taken, val = greedy(foods, max_units, Food.density)
    expected_str = Menu.get_foods_str(taken)
    assert val == 328
    assert expected_str == "wine: <89, 123>; beer: <90, 154>; cola: <79, 150>; apple: <50, 95>; hotdog: <20, 200>; "
