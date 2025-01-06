import math
import random
import numpy as np
from sklearn.linear_model import LogisticRegression

# Minkowski 距離計算
def minkowskiDist(v1, v2, p):
    return sum(abs(a - b) ** p for a, b in zip(v1, v2)) ** (1 / p)

# Animal 類別
class Animal:
    def __init__(self, name, features):
        self.name = name
        self.features = features

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self, other):
        return minkowskiDist(self.features, other.getFeatures(), 2)

    def __str__(self):
        return self.name

# Passenger 類別
class Passenger:
    def __init__(self, p_class, age, gender, label, name):
        self.p_class = p_class
        self.age = age
        self.gender = gender
        self.label = label
        self.name = name

    def getClass(self):
        return self.p_class

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getName(self):
        return self.name

    def getLabel(self):
        return self.label

    def getFeatures(self):
        return [self.p_class, 0, 0, self.age, self.gender]

    def distance(self, other):
        return minkowskiDist(self.getFeatures(), other.getFeatures(), 2)

# Titanic 資料處理函式
def getTitanicData(filename):
    data = {'class': [], 'age': []}
    with open(filename, 'r') as file:
        for line in file:
            p_class, age, *_ = line.strip().split(',')
            data['class'].append(int(p_class))
            data['age'].append(float(age))
    return data

def buildTitanicExamples(filename):
    examples = []
    with open(filename, 'r') as file:
        for line in file:
            p_class, age, gender, label, name = line.strip().split(',')
            examples.append(Passenger(int(p_class), float(age), int(gender), label, name))
    return examples

# 基本函式
def findNearest(instance, examples, dist_func):
    return min(examples, key=lambda x: dist_func(instance.getFeatures(), x.getFeatures(), 2))

def accuracy(tp, tn, fp, fn):
    return tp / (tp + tn + fp + fn)

def sensitivity(tp, fn):
    return tp / (tp + fn)

def specificity(tn, fp):
    return tn / (tn + fp)

def posPredVal(tp, fp):
    return tp / (tp + fp)

def negPredVal(tn, fn):
    return tn / (tn + fn)

def getStats(tp, tn, fp, fn, verbose=False):
    return accuracy(tp, tn, fp, fn), sensitivity(tp, fn), specificity(tn, fp), posPredVal(tp, fp)

def findKNearest(instance, examples, k):
    distances = [(e, minkowskiDist(instance.getFeatures(), e.getFeatures(), 2)) for e in examples]
    distances.sort(key=lambda x: x[1])
    return [e[0] for e in distances[:k]], [e[1] for e in distances[:k]]

def KNearestClassify(training_set, test_set, label, k):
    tp, tn, fp, fn = 0, 0, 0, 0
    for test in test_set:
        neighbors, _ = findKNearest(test, training_set, k)
        predicted_label = max(set([neighbor.getLabel() for neighbor in neighbors]), key=lambda x: [neighbor.getLabel() for neighbor in neighbors].count(x))
        if predicted_label == test.getLabel() == label:
            tp += 1
        elif predicted_label != label and test.getLabel() != label:
            tn += 1
        elif predicted_label == label and test.getLabel() != label:
            fp += 1
        elif predicted_label != label and test.getLabel() == label:
            fn += 1
    return tp, tn, fp, fn

def leaveOneOut(examples, classify_func, verbose=False):
    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(len(examples)):
        training_set = examples[:i] + examples[i+1:]
        test_set = [examples[i]]
        tp_temp, tn_temp, fp_temp, fn_temp = classify_func(training_set, test_set, 'Survived', 3)
        tp += tp_temp
        tn += tn_temp
        fp += fp_temp
        fn += fn_temp
    return tp, tn, fp, fn

def split80_20(examples):
    split_point = int(0.8 * len(examples))
    return examples[:split_point], examples[split_point:]

def randomSplits(examples, classify_func, num_splits, verbose=False):
    results = []
    for _ in range(num_splits):
        random.shuffle(examples)
        training_set, test_set = split80_20(examples)
        results.append(classify_func(training_set, test_set, 'Survived', 3))
    return np.mean(results, axis=0)

def buildModel(examples, verbose=False):
    model = LogisticRegression()
    X = np.array([e.getFeatures() for e in examples])
    y = np.array([1 if e.getLabel() == 'Survived' else 0 for e in examples])
    model.fit(X, y)
    return model

def applyModel(model, examples, label, threshold):
    X = np.array([e.getFeatures() for e in examples])
    predictions = model.predict_proba(X)[:, 1] >= threshold
    tp = sum((pred == 1) and (e.getLabel() == label) for pred, e in zip(predictions, examples))
    fp = sum((pred == 1) and (e.getLabel() != label) for pred, e in zip(predictions, examples))
    tn = sum((pred == 0) and (e.getLabel() != label) for pred, e in zip(predictions, examples))
    fn = sum((pred == 0) and (e.getLabel() == label) for pred, e in zip(predictions, examples))
    return tp, tn, fp, fn

def lr(training_set, test_set, threshold):
    model = buildModel(training_set)
    return applyModel(model, test_set, 'Survived', threshold)

def buildROC(training_set, test_set, label, verbose):
    model = buildModel(training_set)
    thresholds = np.linspace(0, 1, 100)
    tprs, fprs = [], []
    for threshold in thresholds:
        tp, tn, fp, fn = applyModel(model, test_set, label, threshold)
        tprs.append(tp / (tp + fn))
        fprs.append(fp / (fp + tn))
    return np.trapz(tprs, fprs)

