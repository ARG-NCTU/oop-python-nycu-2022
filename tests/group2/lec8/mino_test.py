import pytest
import numpy as np
import random
from lec8_module import get_highs, get_means_and_sds

@pytest.fixture
def sample_data():
    # Generate some sample data for testing
    random.seed(0)
    population = get_highs() 
    sample = random.sample(population, 100)
    return population, sample

def test_get_highs():
    # Test that get_highs returns a list of values
    population = get_highs()
    assert isinstance(population, list)
    # Ensure the length of the list is greater than 0
    assert len(population) > 0
    # Ensure all elements in the list are floats
    assert all(isinstance(x, float) for x in population)

def test_get_means_and_sds(sample_data):
    # Test that get_means_and_sds returns the expected values
    population, sample = sample_data
    pop_mean, sample_mean, pop_sd, sample_sd = get_means_and_sds(population, sample)
    # Check if the means and standard deviations are floats
    assert isinstance(pop_mean, float)
    assert isinstance(sample_mean, float)
    assert isinstance(pop_sd, float)
    assert isinstance(sample_sd, float)
    # Check if the means and standard deviations are within a reasonable range
    assert 0 <= pop_mean <= 40
    assert 0 <= sample_mean <= 40
    assert 0 <= pop_sd <= 20
    assert 0 <= sample_sd <= 20
