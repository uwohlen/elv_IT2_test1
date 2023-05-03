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
smitte = data.iloc[:, 1] 

tid = list(tid)
smitte = list(smitte)

plt.plot(tid, smitte, '.')

def f(t, a, b, c, d):
    # must use pylab functions as they are compatible with the curve_fir function
    return a / (1 + b * math.e ** -(c * t)) + d



[a, b, c, d] = curve_fit(f, [x - start for x in tid], smitte, (145000, 2, 0.05, 126000))[0]
print('a: ', round(a, 2))
print('b:', round(b, 2))
print('c: ', round(c, 3))
print('d: ', round(d, 2))

t = np.linspace(0, slutt - start, (slutt - start) * 100)
plt.plot(t + start, f(t, a, b, c, d), "r")
plt.show()

