import add_path
import mit_ocw_exercises.lec8_classes as lc
import pytest

def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5

def test_team_7_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 5
    assert c.y == 12
    assert c.distance(origin) == 13
    assert origin.distance(c) == 13

def test_11_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
    # Test __str__
    assert str(c) == "<3,4>"

def test_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)
    
def test_12_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
    
def test_5_frac():
    quarter = lc.Fraction(1, 4)
    half = lc.Fraction(1,2)
    assert quarter.num == 1
    assert quarter.denom == 4
    sum = half.__add__(quarter)
    assert sum.num == 6
    assert sum.denom == 8
    
def test_8_coordinate():
    c = lc.Coordinate(6,8)
    origin = lc.Coordinate(0,0)
    assert c.x == 6
    assert c.y == 8
    assert c.distance(origin) == 10
    assert origin.distance(c) == 10
    
    assert not c.x == 7; assert not c.y == 9
def test_16_coordinate():
    a=lc.Coordinate(5,12)
    o=lc.Coordinate(0,0)
    assert a.x==5
    assert a.y==12
    assert a.distance(o)==13
    assert o.distance(a)==13

def test_8_intset():
    myset = lc.intSet() # create a new intSet
    myset.insert(100)
    myset.insert(200)
    myset.insert(300)
    assert myset.member(100) # returns True
    assert not myset.member(400) # returns False
    myset.remove(100)
    assert not myset.member(100) # returns False
    myset.__str__() # returns a string representation of the set

def test_13_coordinate():
    c = lc.Coordinate(14, 48)
    origin = lc.Coordinate(0,0)
    assert c.x == 14
    assert c.y == 48
    assert c.distance(origin) == 50
    assert origin.distance(c) == 50
    
    c = lc.Coordinate(3, 11)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 11
    assert c.distance(origin) == 11.40175425099138
    assert origin.distance(c) == 11.40175425099138

def test_17_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5 

def test_17_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)

def test_7_coordinate():
    c = lc.Coordinate(6, 8)

def test_1_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
  
    a = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0,0)
    assert a.x == 5
    assert a.y == 12
    assert a.distance(origin) == 13
    assert origin.distance(a) == 13
  
    b = lc.Coordinate(9, 40)    
    origin = lc.Coordinate(0,0)    
    assert b.x == 9    
    assert b.y == 40
    assert b.distance(origin) == 41   
    assert origin.distance(b) == 41 


def test_1_intset():  
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)
    
def test_16_coordinate():
    m = lc.Coordinate(7, 24)
    n = lc.Coordinate(0,0)
    assert m.x == 7
    assert m.y == 24
    assert m.distance(n) == 25
    assert n.distance(m) == 25
    s = lc.intSet()
    s.insert(7)
    assert s.member(7)
    s.remove(7)
    assert not s.member(7)
    assert not s.member(9)

def test_6_coordinate():
    c = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0,0)
    assert c.x == 5
    assert c.y == 12
    assert c.distance(origin) == 13
    assert origin.distance(c) == 13
    
def test_14_coordinate():
    s = lc.Coordinate(8, 15)
    origin = lc.Coordinate(0,0)
    assert s.x == 8
    assert s.y == 15
    assert s.distance(origin) == 17
    assert origin.distance(s) == 17
    
def test_9_coordinate():
    c = lc.Coordinate(6,8)
    origin = lc.Coordinate(0,0)
    assert c.x == 6
    assert c.y == 8
    assert c.distance(origin) == 10
    assert origin.distance(c) == 10



def test_5_Fraction():
    a = lc.Fraction(1,2)
    assert a.__float__() == 0.5
    assert a.__str__() == '1/2'
    
    
    

def test_7_intset():
    s = lc.intSet()
    s.insert(7)
    s.insert(9)
    assert s.member(7)
    assert s.member(9)
    assert not s.member(10)
    s.remove(7)
    assert not s.member(7)
    assert s.member(9)


def test_9_intset():
    s = lc.intSet()
    s.insert(8)
    s.insert(7)
    assert s.member(8)
    assert s.member(7)
    s.remove(8)
    assert not s.member(8)
    assert s.member(7)

def test_4_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
  
def test_4_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)


def test_2_Fraction():
    p = lc.Fraction(2, 5)
    assert p.num == 2
    assert p.denom == 5
    q = lc.Fraction(1, 5)
    assert q.num == 1
    assert q.denom == 5
    a1 = p + q
    assert str(a1) == "15/25"
    a2 = p - q
    assert str(a2) == "5/25"
    assert lc.Fraction.__float__(p) == 0.4
    assert str(p.inverse()) == "5/2"

def test_7_coordinate():
    c = lc.Coordinate(3,4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5

def test_7_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)

if __name__ == "__main__":  #Updated by group2
    test_coordinate()
    print("test_coordinate passed")
    test_intset()
    print("test_intset passed")
    test_2_Fraction()
    print("test_2_Fraction passed")
    print("All tests passed")

def test_11_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5

def test_11_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    
def test_17_coordinate():
    c = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0,0)
    assert c.x == 5
    assert c.y == 12
    assert c.distance(origin) == 13
    assert origin.distance(c) == 13

def test_12_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)
