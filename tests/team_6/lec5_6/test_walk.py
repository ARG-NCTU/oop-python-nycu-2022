import pytest
from random import seed
from lec5_module import walk, sim_walks, UsualDrunk, MasochistDrunk, Field, Location


@pytest.fixture
def usual_drunk():
    return UsualDrunk()


@pytest.fixture
def masochist_drunk():
    return MasochistDrunk()


@pytest.fixture
def field():
    return Field()

@pytest.fixture
def num_steps():
    return [110, 100, 1000, 10000]

def test_walk(usual_drunk, field):
    seed(0)  # set random seed for reproducibility
    start_loc = Location(0, 0)
    field.add_drunk(usual_drunk, start_loc)
    assert walk(field, usual_drunk, 0) == 0.0  # test 0 steps
    assert walk(field, usual_drunk, 1) == 1.0  # test 1 step
    assert walk(field, usual_drunk, 10) == pytest.approx(1.41, abs=0.01)  # test 10 steps
    assert walk(field, usual_drunk, 100) == pytest.approx(11.31, abs=0.1)  # test 100 steps


def test_sim_walks(usual_drunk, masochist_drunk, field):
    seed(0)  # set random seed for reproducibility
    usual_distances = sim_walks(10, 10, UsualDrunk)
    masochist_distances = sim_walks(10, 10, MasochistDrunk)
    assert len(usual_distances) == 10  # test length of returned list
    assert len(masochist_distances) == 10  # test length of returned list
    assert isinstance(usual_distances[0], float)  # test type of list elements
    assert isinstance(masochist_distances[0], float)  # test type of list elements
    assert all(isinstance(d, float) for d in usual_distances)  # test type of all list elements
    assert all(isinstance(d, float) for d in masochist_distances)  # test type of all list elements
    assert all(d >= 0 for d in usual_distances)  # test non-negative distances
    assert all(d >= 0 for d in masochist_distances)  # test non-negative distances
    assert usual_distances != masochist_distances  # test that the two types of drunks give different results

def test_sim_walks_num_steps(num_steps):
    for n in num_steps:
        distances = sim_walks(n, 10, UsualDrunk)
        assert len(distances) == 10
