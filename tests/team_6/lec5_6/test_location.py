import pytest
from lec5_module import Location

def test_location():
    # Test the Location class
    loc1 = Location(0, 0)
    assert loc1.get_x() == 0
    assert loc1.get_y() == 0

    loc2 = Location(1, 1)
    assert loc2.get_x() == 1
    assert loc2.get_y() == 1

    loc3 = loc1.move(2, 3)
    assert loc3.get_x() == 2
    assert loc3.get_y() == 3

    loc4 = loc2.move(-1, -1)
    assert loc4.get_x() == 0
    assert loc4.get_y() == 0

    assert loc1.dist_from(loc2) == pytest.approx(1.41421356237, rel=1e-9)
    assert loc1.dist_from(loc3) == pytest.approx(3.60555127546, rel=1e-9)
    assert loc2.dist_from(loc3) == pytest.approx(2.23606797749, rel=1e-9)

    assert str(loc1) == '<0, 0>'
    assert str(loc2) == '<1, 1>'
    assert str(loc3) == '<2, 3>'
    assert str(loc4) == '<0, 0>'

def get_6_locations():
    loca = Location(0, 0)
    assert loca.get_x() == 0
    assert loca.get_y() == 0

    locb = Location(3, 4)
    assert locb.get_x() == 3
    assert locb.get_y() == 4

    locc = loca.move(5, 12)
    assert locc.get_x() == 5
    assert locc.get_y() == 12

    locd = locb.move(-1, 4)
    assert locd.get_x() == 2
    assert locd.get_y() == 8

    assert loca.dist_from(locb) == pytest.approx(5.0, rel=1e-9)
    assert loca.dist_from(locc) == pytest.approx(13.0, rel=1e-9)
    assert locb.dist_from(locc) == pytest.approx(10.0, rel=1e-9)

    assert str(loca) == '<0, 0>'
    assert str(locb) == '<3, 4>'
    assert str(locc) == '<5, 12>'
    assert str(locd) == '<2, 8>'


