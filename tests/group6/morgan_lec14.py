import pytest
import add_path
import random

from mit_ocw_data_science.lec13.lecture13 import *

def test_minkowskiDist():
    assert minkowskiDist([0,0], [3,4], 2) == 5.0
    assert minkowskiDist([1,2,3], [4,5,6], 1) == 9.0
    assert minkowskiDist([1,2,3], [4,5,6], 2) == 5.196152422706632
    assert minkowskiDist([1,2,3], [4,5,6], 3) == 4.3267487109222245
    
def test_passenger_distance():
    # Test distance between two passengers
    p1 = Passenger(1, 25, 1, "Survived", "Test Passenger 1")
    p2 = Passenger(2, 30, 0, "Died", "Test Passenger 2")
    dist = p1.distance(p2)
    assert round(dist, 2) == 5.29, f"Distance calculation failed: {dist}"
    print("Passenger distance test passed.")

def test_titanic_data_loading():
    # Test Titanic data loading function
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert len(examples) > 0, "Failed to load Titanic data"
    print("Titanic data loading test passed.")
    
def test_knn_classification():
    # Run a basic KNN classification
    examples = buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = split80_20(examples)
    truePos, falsePos, trueNeg, falseNeg = KNearestClassify(trainingSet, testSet, 'Survived', k=3)
    
    # Verify that the output makes sense
    accuracy = (truePos + trueNeg) / (truePos + falsePos + trueNeg + falseNeg)
    assert 0 <= accuracy <= 1, f"Accuracy out of bounds: {accuracy}"
    print("KNN classification test passed.")
    
    # Display statistics
    getStats(truePos, falsePos, trueNeg, falseNeg)

def run_all_tests():
    print("Running tests...")
    test_minkowskiDist()
    test_passenger_distance()
    test_titanic_data_loading()
    test_knn_classification()
    print("All tests completed.")
