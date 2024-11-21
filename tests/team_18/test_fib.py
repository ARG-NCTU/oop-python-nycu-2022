import add_path
import fib_9 as lc
import pytest

def test_fib():
    a=lc.Fibo()
    assert a.cal(10) == 55
    assert a.cal(20) == 6765
    assert a.cal(30) == 832040
