import pytest
import add_path
import random
from mit_ocw_data_science.lec11.lec11_module import *
import numpy as np
import time


def test_variance():  #with denomiator = n
    assert variance([1, 2, 3, 4, 5]) == 2.0
    assert variance([1, 2, 3, 4, 5, 6]) == 2.9166666666666665
    assert variance([1, 2, 3, 4, 5, 6, 7]) == 4.0
    assert variance([1, 2, 3, 4, 5, 6, 7, 8]) == 5.25
    assert variance([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 6.666666666666667 
    assert variance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8.25
    assert variance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10.0
    
def test_variance_negative():  #with denomiator = n
    assert variance([-1,-2,-3,-4,-5]) == 2.0
    assert variance([-1,-2,-3,-4,-5,-6]) == 2.9166666666666665
    assert variance([-1,-2,-3,-4,-5,-6,-7]) == 4.0
    assert variance([-1,-2,-3,-4,-5,-6,-7,-8]) == 5.25
    assert variance([-1,-2,-3,-4,-5,-6,-7,-8,-9]) == 6.666666666666667 
    assert variance([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]) == 8.25
    assert variance([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11]) == 10.0
    
def test_variance_random(): #with denomiator = n
    for i in range(1000):
        n = random.randint(1,100)
        X = [random.randint(0,100) for i in range(n)]
        assert variance(X) == sum([(x - sum(X)/n)**2 for x in X])/n

# Test variance with single element
def test_variance_single_element():
    assert variance([1]) == 0.0
    assert variance([-1]) == 0.0
    assert variance([0]) == 0.0
    assert variance([100]) == 0.0

# Test variance with all same elements
def test_variance_all_same_elements():
    assert variance([2, 2, 2, 2, 2]) == 0.0
    assert variance([-2, -2, -2, -2, -2]) == 0.0
    assert variance([0, 0, 0, 0, 0]) == 0.0
    
def test_minkowskiDist_p(): #v1 = [1,2,3] v2 = [4,5,6] p = 1~10
    v1 = [1,2,3]
    v2 = [4,5,6]
    for i in range(1,11):
        assert minkowskiDist(v1, v2, i) == pytest.approx(np.linalg.norm(np.array(v1) - np.array(v2), ord=i))
    
                                                                  
def test_minkowskiDist_random():
    for i in range(1000):
        v1 = [random.randint(0,100) for i in range(100)]
        v2 = [random.randint(0,100) for i in range(100)]
        p = random.randint(1,100)
        assert minkowskiDist(v1, v2, p) == pytest.approx(np.linalg.norm(np.array(v1) - np.array(v2), ord=p))
