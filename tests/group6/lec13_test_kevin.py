import pytest
import lecture13
import random
import sklearn.linear_model
import pytest

def test_minkowskiDist():   
    assert minkowskiDist([1,2,3], [4,5,6], 1) == 9
    assert minkowskiDist([1,2,3], [4,5,6], 2) == 5.196152422706632
    assert minkowskiDist([1,2,3], [4,5,6], 3) == 4.3267487109222245
    assert minkowskiDist([1,2,3], [4,5,6], 4) == 4.06201920231798
    assert minkowskiDist([1,2,3], [4,5,6], 5) == 3.912893032168255
    assert minkowskiDist([1,2,3], [4,5,6], 6) == 3.801032687666573
    assert minkowskiDist([1,2,3], [4,5,6], 7) == 3.713695681834933
    assert minkowskiDist([1,2,3], [4,5,6], 8) == 3.643532574250745
    assert minkowskiDist([1,2,3], [4,5,6], 9) == 3.586464622934501
def test_animal_class():
    cobra = Animal('cobra', [1,1,1,1,0])
    assert cobra.getName() == 'cobra'
    assert cobra.getFeatures() == [1,1,1,1,0]
    assert cobra.distance(Animal('rattlesnake', [1,1,1,1,0])) == 0.0
    assert cobra.__str__() == 'cobra'
def test_passenger_class():
    p = Passenger(1, 20, 1, 'Survived', 'John')
    assert p.distance(Passenger(1, 20, 1, 'Survived', 'John')) == 0.0
    assert p.getClass() == 1
    assert p.getAge() == 20
    assert p.getGender() == 1
    assert p.getName() == 'John'
    assert p.getFeatures() == [1, 0, 0, 20, 1]
    assert p.getLabel() == 'Survived'
def test_getTitanicData():
    data = getTitanicData('TitanicPassengers.txt')
    assert data['class'] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert data['age'] == [29.0, 0.9167, 2.0, 30.0, 25.0, 48.0, 63.0, 39.0, 53.0, 71.0]
def test_buildTitanicExamples():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert len(examples) == 10
    assert examples[0].getFeatures() == [1, 0, 0, 29.0, 1]
    assert examples[0].getLabel() == 'Survived'
def test_findNearest():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert findNearest('John', examples, minkowskiDist) == examples[0]
def test_accuracy():
    assert accuracy(1, 2, 3, 4) == 0.25
def test_sensitivity():
    assert sensitivity(1, 2) == 0.3333333333333333
def test_specificity():
    assert specificity(1, 2) == 0.3333333333333333
def test_posPredVal():
    assert posPredVal(1, 2) == 0.3333333333333333
def test_negPredVal():
    assert negPredVal(1, 2) == 0.3333333333333333
def test_getStats():
    assert getStats(1, 2, 3, 4, False) == (0.25, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333)

def test_findKNearest():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert findKNearest(examples[0], examples, 3) == ([examples[0], examples[1], examples[2]], [0.0, 0.0833, 0.0833])
def test_KNearestClassify():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert KNearestClassify(examples, examples, 'Survived', 3) == (10, 0, 0, 0)
def test_leaveOneOut():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert leaveOneOut(examples, KNearestClassify, False) == (10, 0, 0, 0)
def test_split80_20():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = split80_20(examples)
    assert len(trainingSet) == 8
    assert len(testSet) == 2
def test_randomSplits():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert randomSplits(examples, KNearestClassify, 10, False) == (10, 0, 0, 0)
def test_buildModel():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert buildModel(examples, False).classes_ == ['Died' 'Survived']
def test_applyModel():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    model = buildModel(examples, False)
    assert applyModel(model, examples, 'Survived', 0.5) == (10, 0, 0, 0)
def test_lr():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    assert lr(examples, examples, 0.5) == (10, 0, 0, 0)
def test_buildROC():
    examples = buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = split80_20(examples)
    assert buildROC(trainingSet, testSet, 'Title', False) == 1.0
    
