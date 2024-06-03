import pytest
from lec5_module import Field,  Drunk, UsualDrunk, MasochistDrunk, Location

def test_usual_drunk():
    # Test taking a step
    d = UsualDrunk()
    for i in range(10):
        step = d.take_step()
        assert step in [(0, 1), (0, -1), (1, 0), (-1, 0)]

def test_masochist_drunk():
    # Test taking a step
    d = MasochistDrunk()
    for i in range(10):
        step = d.take_step()
        assert step in [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
