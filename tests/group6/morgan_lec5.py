import pytest

# 函式實現
def quotient_and_remainder(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return (x // y, x % y)

def sum_elem_method1(lst):
    return sum(lst)

def sum_elem_method2(lst):
    total = 0
    for elem in lst:
        total += elem
    return total

# 測試函式
def test_quotient_and_remainder():
    assert quotient_and_remainder(27, 6) == (4, 3)
    assert quotient_and_remainder(20, 7) == (2, 6)
    assert quotient_and_remainder(25, 8) == (3, 1)
    assert quotient_and_remainder(27, 9) == (3, 0)
    assert quotient_and_remainder(22, 10) == (2, 2)
    assert quotient_and_remainder(28, 11) == (2, 6)

def test_quotient_and_remainder_zero_division():
    with pytest.raises(ZeroDivisionError):
        quotient_and_remainder(20, 0)

def test_sum_elem_method1():
    assert sum_elem_method1([1, 2, 3, 6]) == 12
    assert sum_elem_method1([-1, -7, -3, -4]) == -15
    assert sum_elem_method1([13, 34, 0, 84, 95, 0, 9]) == 235
    assert sum_elem_method1([7]) == 7
    assert sum_elem_method1([]) == 0

def test_sum_elem_method2():
    assert sum_elem_method2([1, 5, 3, 4]) == 13
    assert sum_elem_method2([-1, -8, -7, -4]) == -20
    assert sum_elem_method2([13, 34, 0, 84, 95, 0, 9]) == 235
    assert sum_elem_method2([8]) == 8
    assert sum_elem_method2([]) == 0

def test_quotient_and_remainder_additional():
    assert quotient_and_remainder(24, 6) == (4, 0)
    assert quotient_and_remainder(20, 7) == (2, 6)
    assert quotient_and_remainder(13, 8) == (1, 5)
    assert quotient_and_remainder(30, 9) == (3, 3)
    assert quotient_and_remainder(16, 10) == (1, 6)

    with pytest.raises(ZeroDivisionError):
        quotient_and_remainder(11, 0)

# 如果直接執行此檔案，運行測試
if __name__ == "__main__":
    pytest.main()

