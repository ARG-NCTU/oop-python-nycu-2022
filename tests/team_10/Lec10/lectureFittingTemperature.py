import random
import matplotlib.pyplot as plt
import numpy as np

# Set line width
plt.rcParams['lines.linewidth'] = 4
# Set font size for titles 
plt.rcParams['axes.titlesize'] = 20
# Set font size for labels on axes
plt.rcParams['axes.labelsize'] = 20
# Set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
# Set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
# Set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
# Set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
# Set size of markers
plt.rcParams['lines.markersize'] = 10
# Set number of examples shown in legends
plt.rcParams['legend.numpoints'] = 1

def getData(fileName):
    distances = []
    masses = []
    with open(fileName, 'r') as dataFile:
        dataFile.readline()  # discard header
        for line in dataFile:
            x, y = line.split()
            distances.append(float(x))
            masses.append(float(y))
    return distances, masses

def labelPlot():
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = np.array(xVals)
    yVals = np.array(yVals)
    xVals = xVals * 9.81  # due to gravity
    plt.plot(xVals, yVals, 'bo', label='Measured displacements')
    labelPlot()

def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = np.array(xVals)
    yVals = np.array(yVals)
    xVals = xVals * 9.81  # get force
    plt.plot(xVals, yVals, 'bo', label='Measured points')
    labelPlot()
    a, b = np.polyfit(xVals, yVals, 1)
    estYVals = a * np.array(xVals) + b
    print('a =', a, 'b =', b)
    plt.plot(xVals, estYVals, 'r', label='Linear fit, k = ' + str(round(1 / a, 5)))
    plt.legend(loc='best')

def fitData1(fileName):
    xVals, yVals = getData(fileName)
    xVals = np.array(xVals)
    yVals = np.array(yVals)
    xVals = xVals * 9.81  # get force
    plt.plot(xVals, yVals, 'bo', label='Measured points')
    labelPlot()
    model = np.polyfit(xVals, yVals, 1)
    estYVals = np.polyval(model, xVals)
    plt.plot(xVals, estYVals, 'r', label='Linear fit, k = ' + str(round(1 / model[0], 5)))
    plt.legend(loc='best')

def rSquared(observed, predicted):
    error = ((predicted - observed) ** 2).sum()
    meanError = error / len(observed)
    return 1 - (meanError / np.var(observed))

def genFits(xVals, yVals, degrees):
    models = []
    for d in degrees:
        model = np.polyfit(xVals, yVals, d)
        models.append(model)
    return models

def plotFits(models, degrees, xVals, yVals, title):
    plt.plot(xVals, yVals, 'o', label='Data')
    for i in range(len(models)):
        estYVals = np.polyval(models[i], xVals)
        error = rSquared(yVals, estYVals)
        plt.plot(xVals, estYVals, label='Fit of degree ' + str(degrees[i]) + ', R2 = ' + str(round(error, 5)))
    plt.legend(loc='best')
    plt.title(title)

def genNoisyParabolicData(a, b, c, xVals, fName):
    yVals = []
    for x in xVals:
        theoreticalVal = a * x ** 2 + b * x + c
        yVals.append(theoreticalVal + random.gauss(0, 35))
    with open(fName, 'w') as f:
        f.write('x y\n')
        for i in range(len(xVals)):
            f.write(f"{xVals[i]} {yVals[i]}\n")

# Generate sample data
xVals = [i for i in range(30)]
genNoisyParabolicData(2, -3, 5, xVals, 'sampleData.txt')

# Plot the data and fit a linear model
plt.figure()
plotData('sampleData.txt')
fitData('sampleData.txt')
plt.show()

