import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest


# please write a test for quotient_and_remainder function
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(27, 6) == (4, 3)
    assert lec5.quotient_and_remainder(20, 7) == (2, 6)
    assert lec5.quotient_and_remainder(25, 8) == (3, 1)
    assert lec5.quotient_and_remainder(27, 9) == (3, 0)
    assert lec5.quotient_and_remainder(22, 10) == (2, 2)
    assert lec5.quotient_and_remainder(28, 11) == (2, 6)

    try:
        lec5.quotient_and_remainder(20, 0)
    except ZeroDivisionError:
         print("ZeroDivisionError")
    assert lec5.quotient_and_remainder(15, 11) == (1, 4)


def test_sum_elem_method1():
    assert lec5.sum_elem_method1([1, 2, 3, 6]) == 10
    assert lec5.sum_elem_method1([-1, -7, -3, -4]) == -15
    assert lec5.sum_elem_method1([13, 34, 0, 84, 95, 0, 9]) == 235
    assert lec5.sum_elem_method1([7]) == 7
    assert lec5.sum_elem_method1([]) == 0


def test_sum_elem_method2():
    assert lec5.sum_elem_method2([1, 5, 3, 4]) == 13
    assert lec5.sum_elem_method2([-1, -8, -7, -4]) == -20
    assert lec5.sum_elem_method2([13, 34, 0, 84, 95, 0, 9]) == 235
    assert lec5.sum_elem_method2([8]) == 8
    assert lec5.sum_elem_method2([]) == 0

def new_test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(24, 6) == (4, 0)
    assert lec5.quotient_and_remainder(20, 7) == (2, 6)
    assert lec5.quotient_and_remainder(13, 8) == (1, 5)
    assert lec5.quotient_and_remainder(30, 9) == (3, 3)
    assert lec5.quotient_and_remainder(16, 10) == (1, 6)

    try:
        lec5.quotient_and_remainder(11, 0)
    except ZeroDivisionError:
         print("ZeroDivisionError")
    assert lec5.quotient_and_remainder(23, 15) == (1, 8)
