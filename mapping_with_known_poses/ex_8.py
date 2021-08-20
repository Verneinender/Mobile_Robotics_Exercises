# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:40:12 2021

@author: wangy
"""
import numpy as np
import matplotlib.pyplot as plt




def inv_sensor_model(z, c):
    #i = int(z/10)
    if c > z - 10 and c < z + 20 :
        return np.log(0.6/0.4)
    elif c <= z - 10:
        return np.log(0.3/0.7)
    return 0

c = range(0,201,10)
logodds = np.zeros(len(c))

meas = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]

prior = np.log(0.5/0.5)

for i in range(len(meas)):
    for j in range(len(c)):
        logodds[j] = logodds[j] + inv_sensor_model(meas[i], c[j]) - prior

m = 1 - 1./(1 + np.exp(logodds))

plt.plot(c, m)
plt.xlabel("x-position [cm]")
plt.ylabel("occupancy p(x)")
plt.savefig("sheet_08_ex2")
plt.show()
