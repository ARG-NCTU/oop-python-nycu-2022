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
    # Test that get_highs returns the expected list of values
    population = get_highs()
    expected = [3.1, 0.55, 0.0] 
    assert population[0:3] == expected

def test_get_means_and_sds(sample_data):
    # Test that get_means_and_sds returns the expected values
    population, sample = sample_data
    pop_mean, sample_mean, pop_sd, sample_sd = \
        get_means_and_sds(population, sample)
    expected_pop_mean = np.mean(population)
    expected_sample_mean = np.mean(sample)
    expected_pop_sd = np.std(population)
    expected_sample_sd = np.std(sample)
    assert pop_mean == expected_pop_mean
    assert sample_mean == expected_sample_mean
    assert pop_sd == expected_pop_sd
    assert sample_sd == expected_sample_sd

