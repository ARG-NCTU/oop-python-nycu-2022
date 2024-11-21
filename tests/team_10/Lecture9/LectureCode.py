import random
import pylab
import numpy as np

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers
pylab.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline() #discard header
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def labelPlot():
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81  # due to gravity
    pylab.plot(xVals, yVals, 'bo', label='Measured displacements')
    labelPlot()

def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81 #get force
    pylab.plot(xVals, yVals, 'bo', label='Measured points')
    labelPlot()
    a, b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a * pylab.array(xVals) + b
    print('a =', a, 'b =', b)
    pylab.plot(xVals, estYVals, 'r', label='Linear fit, k = ' + str(round(1/a, 5)))
    pylab.legend(loc='best')

def fitData1(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81 #get force
    pylab.plot(xVals, yVals, 'bo', label='Measured points')
    labelPlot()
    model = pylab.polyfit(xVals, yVals, 1)
    estYVals = pylab.polyval(model, xVals)
    pylab.plot(xVals, estYVals, 'r', label='Linear fit, k = ' + str(round(1/model[0], 5)))
    pylab.legend(loc='best')

def aveMeanSquareError(data, predicted):
    error = 0.0
    for i in range(len(data)):
        error += (data[i] - predicted[i])**2
    return error / len(data)

def rSquared(observed, predicted):
    error = ((predicted - observed) ** 2).sum()
    meanError = error / len(observed)
    return 1 - (meanError / np.var(observed))

def genFits(xVals, yVals, degrees):
    models = []
    for d in degrees:
        model = pylab.polyfit(xVals, yVals, d)
        models.append(model)
    return models

def evaluateFits(models, degrees, xVals, yVals, title):
    pylab.plot(xVals, yVals, 'o', label='Data')
    for i in range(len(models)):
        estYVals = pylab.polyval(models[i], xVals)
        error = rSquared(yVals, estYVals)
        pylab.plot(xVals, estYVals, label='Fit of degree ' + str(degrees[i]) + ', R2 = ' + str(round(error, 5)))
    pylab.legend(loc='best')
    pylab.title(title)

xVals, yVals = getData('mysteryData.txt')
degrees = (1, 2)
models = genFits(xVals, yVals, degrees)
evaluateFits(models, degrees, xVals, yVals, 'Mystery Data')

degrees = (2, 4, 8, 16)
models = genFits(xVals, yVals, degrees)
evaluateFits(models, degrees, xVals, yVals, 'Mystery Data')

def genNoisyParabolicData(a, b, c, xVals, fName):
    yVals = []
    for x in xVals:
        theoreticalVal = a * x**2 + b * x + c
        yVals.append(theoreticalVal + random.gauss(0, 35))
    with open(fName, 'w') as f:
        f.write('x        y\n')
        for i in range(len(yVals)):
            f.write(str(xVals[i]) + ' ' + str(yVals[i]) + '\n')

if __name__ == "__main__":
    # Uncomment to generate noisy parabolic data
    # genNoisyParabolicData(3, 2, 1, range(-10, 11), 'noisyParabolicData.txt')
    pass

