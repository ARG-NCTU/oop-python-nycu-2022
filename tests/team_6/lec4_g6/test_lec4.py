import random
import pytest
import math
from lec4_module import roll_die, run_sim, same_date, birthday_prob


def test_roll_die():
    # Test that the function returns an int between 1 and 6
    for i in range(100):
        result = roll_die()
        assert isinstance(result, int)
        assert result >= 1 and result <= 6

def test_roll():
    n = 10
    result = ''
    for i in range(n):
        result = result + str(roll_die())
    print(f'test_roll: {result}')

def test_run_sim():
    # Test with a known goal and numTrials
    random.seed(0)
    goal = '11111'
    num_trials = 1000
    run_sim(goal, num_trials, '11111')

def test_same_date():
    # Test with known values for numPeople and numSame
    random.seed(0)
    num_people = 23
    num_same = 2
    result = same_date(num_people, num_same)
    assert isinstance(result, bool)
    assert result == True

def test_birthday_prob():
    # Test with known values for numPeople, numSame, and numTrials
    random.seed(0)
    num_people = 23
    num_same = 2
    num_trials = 1000
    result = birthday_prob(num_people, num_same, num_trials)
    assert isinstance(result, float)
    assert result == pytest.approx(0.507, abs=0.05)

def test_birthday_prob_more():
    random.seed(0)
    for num_people in [10, 20, 40, 100]:
        print('For', num_people,
              'est. prob. of a shared birthday is',
              birthday_prob(num_people, 2, 10000))
        numerator = math.factorial(366)
        denom = (366 ** num_people) * math.factorial(366 - num_people)
        print('Actual prob. for N = 100 =',
              1 - numerator / denom)
