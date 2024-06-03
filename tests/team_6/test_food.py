import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("apple", 10, 50)

def test_get_value(food):
    assert food.get_value() == 10

def test_get_cost(food):
    assert food.get_cost() == 50

def test_density(food):
    assert food.density() == 0.2

def test_str(food):
    assert str(food) == "apple: <10, 50>"

def food_6():
    return Food("calculus", 20, 500)

def test_get_value_6():
    assert food_6().get_value() == 20

def test_get_cost_6():
    assert food_6().get_cost() == 500

def test_density_6():
    assert food_6().density() == 0.04

def test_str_6():
    assert str(food_6()) == "calculus: <20, 500>"

