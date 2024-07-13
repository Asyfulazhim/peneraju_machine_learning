# Data Collection
# Data preparation
# Exploratory Data Analysis (EDA) 1) Descriptive Statistics  2) Inferential Statistics
# Mean (average)
# Median (sorting all number, and the number at the middle) 
# Mode (which number appear frequently)
# STD - define how far away you from average
# Variance - how far away you from average squared
# Quartile -
# IQR - Interquartile range - 3rd quartile - 1st quart
# Bell curve
# Data Visualization 
import time
import numpy as np
quantities = [10, 20, 30 ,40 ,50]
newquantities = [5, 15, 25, 35, 45]
totalquantities = zip(quantities,newquantities)
print(totalquantities)
print(list(totalquantities))
totalquantities = [x + y for x,y in zip(quantities, newquantities)]
print(totalquantities)


size = 10**6
a = range (0,size)
b = range (0,size)
numpya = np.arange(0,size)
numpyb = np.arange(0,size)

starttime = time.time()
c = [x + y for x,y in zip(a,b)]
print(time.time() - starttime)

starttime = time.time()
d = numpya + numpyb
print(time.time() - starttime)

print(c[0:10])
print(d[0:10])
