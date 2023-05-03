from matplotlib import pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit
import pandas as pd

start = 0
slutt = 400


data = pd.read_csv('C:/Users/alska048/Documents/Matte/R2/ModelleringProsjekt/smittetallNorge.csv', header = None, skiprows = 1, sep = ';')
print(data)

data = data[(data[0] >= start) & (data[0] <= slutt)] # define the ranges of the data set we want
tid = data.iloc[:, 0] # make a list of all the values in the column with index 2
smitte = data.iloc[:, 2] 

tid = list(tid)
smitte = list(smitte)

plt.plot(tid, smitte, '.')

def f(t, a, b, c):
    # must use pylab functions as they are compatible with the curve_fir function
    return a * math.e ** (-(t-b)**2/(2*c**2))



[a, b, c] = curve_fit(f, [x - start for x in tid], smitte, (25000, 250, 400))[0]
print('a: ', round(a, 2))
print('b:', round(b, 2))
print('c: ', round(c, 3))
#print('d: ', round(d, 3))

t = np.linspace(0, slutt - start, (slutt - start) * 100)
plt.plot(t + start, f(t, a, b, c), "r")
plt.show()


x = list(tid.copy())
y = []
regress = []

def trapes(a, b, func, dx):
    riemann = 0
    for i in np.arange(a, b, dx):
        riemann += 0.5 * (func(i) + func(i + dx)) * dx
    return riemann

def func(t):
    return 19380.54 * math.e ** (-(t-245.71)**2/(2*22.7**2))


def reg(t):
    return 1278992.71 / (1 + 337499.59 * math.e ** -(0.053 * t)) + 169552.95

for i in range(0, len(x)):
    y.append(trapes(0, i, func, 0.1) + 169552.95)
    regress.append(reg(i))
    
plt.plot(x, y, '-',label='Gaussian')
plt.plot(x, regress, '-', label='regresjon')
plt.show()
