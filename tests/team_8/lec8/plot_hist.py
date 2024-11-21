import matplotlib.pyplot as plt
from lec8_module import *

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


population = get_highs()
sample = random.sample(population, 100)
pop_mean, sample_mean, pop_sd, sample_sd = \
    get_means_and_sds(population, sample, True)


