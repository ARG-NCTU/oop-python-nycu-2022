
import add_path
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6
import pytest

# please write a test for fib function
def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89
    assert lec6.fib(11) == 144
    assert lec6.fib(12) == 233
    assert lec6.fib(13) == 377
    assert lec6.fib(14) == 610
    assert lec6.fib(15) == 987
    assert lec6.fib(16) == 1597
    assert lec6.fib(17) == 2584
    assert lec6.fib(18) == 4181
    assert lec6.fib(19) == 6765
    assert lec6.fib(20) == 10946
    assert lec6.fib(21) == 17711
    assert lec6.fib(22) == 28657
    assert lec6.fib(23) == 46368
    assert lec6.fib(24) == 75025
    assert lec6.fib(25) == 121393
    assert lec6.fib(26) == 196418
    assert lec6.fib(27) == 317811
    assert lec6.fib(28) == 514229
    assert lec6.fib(29) == 832040
    assert lec6.fib(30) == 1346269
    assert lec6.fib(31) == 2178309
    assert lec6.fib(32) == 3524578
    assert lec6.fib(33) == 5702887
    assert lec6.fib(34) == 9227465
    assert lec6.fib(35) == 14930352
    assert lec6.fib(36) == 24157817
    assert lec6.fib(37) == 39088169
    assert lec6.fib(38) == 63245986
    assert lec6.fib(39) == 102334155
    assert lec6.fib(40) == 165580141
    assert lec6.fib(41) == 267914296
    assert lec6.fib(42) == 433494437
    assert lec6.fib(43) == 701408733
    assert lec6.fib(44) == 1134903170
    assert lec6.fib(45) == 1836311903
    assert lec6.fib(46) == 2971215073
    assert lec6.fib(47) == 4807526976
    assert lec6.fib(48) == 7778742049
    assert lec6.fib(49) == 12586269025
    assert lec6.fib(50) == 20365011074
    assert lec6.fib(51) == 32951280099
    assert lec6.fib(52) == 53316291173
    assert lec6.fib(53) == 86267571272
    assert lec6.fib(54) == 139583862445
    assert lec6.fib(55) == 225851433717
    assert lec6.fib(56) == 365435296162
    assert lec6.fib(57) == 591286729879
    assert lec6.fib(58) == 956722026041
    assert lec6.fib(59) == 1548008755920


# please write a test for is_palindrome function
def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True


