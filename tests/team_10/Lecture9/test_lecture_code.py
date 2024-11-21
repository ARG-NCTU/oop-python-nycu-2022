import pytest
import pylab
import numpy as np
from LectureCode import getData, genFits, evaluateFits, rSquared

def test_rSquared():
    # Test the rSquared function
    observed = np.array([1, 2, 3, 4, 5])
    predicted = np.array([1, 2, 3, 4, 5])
    assert rSquared(observed, predicted) == 1.0

    predicted = np.array([1, 2, 3, 4, 6])
    assert rSquared(observed, predicted) < 1.0

def test_evaluateFits():
    # Use a small dataset for testing
    xVals, yVals = getData('mysteryData.txt')
    degrees = [1, 2]
    models = genFits(xVals, yVals, degrees)
    
    pylab.figure()
    evaluateFits(models, degrees, xVals, yVals, 'Test Data')
    # Save the figure to a file to check if it runs without error
    pylab.savefig('/tmp/test_evaluateFits.png')

    # You can add more specific checks here if needed

if __name__ == "__main__":
    pytest.main()

