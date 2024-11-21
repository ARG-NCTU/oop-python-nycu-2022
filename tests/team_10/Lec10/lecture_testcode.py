# test_lectureCode.py

import pytest
import numpy as np
from lectureCode import getData, rSquared, genFits

# Sample data for testing
test_data = """x y
0.0 0.0
1.0 9.81
2.0 19.62
3.0 29.43
4.0 39.24
5.0 49.05
"""


def create_test_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)

def test_getData():
    create_test_file('test_data.txt', test_data)
    distances, masses = getData('test_data.txt')
    assert distances == [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    assert masses == [0.0, 9.81, 19.62, 29.43, 39.24, 49.05]

def test_rSquared():
    observed = np.array([0, 1, 2, 3, 4, 5])
    predicted = np.array([0, 1, 2, 3, 4, 5])
    assert rSquared(observed, predicted) == 1.0
    predicted = np.array([0, 1, 1.5, 3.5, 4, 5])
    assert round(rSquared(observed, predicted), 2) == 0.97

def test_genFits():
    create_test_file('test_data.txt', test_data)
    distances, masses = getData('test_data.txt')
    models = genFits(np.array(distances) * 9.81, np.array(masses), [1])
    assert len(models) == 1
    assert round(models[0][0], 2) == 1.00
    assert round(models[0][1], 2) == 0.00

