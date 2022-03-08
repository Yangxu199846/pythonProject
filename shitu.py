import matplotlib.pyplot as plt
from numpy import *
t = linspace(0,10,50)
x = sin(t)
y = cos(t)
plt.plot(x)
plt.plot(y)
plt.legend(['sinx','cosx'])
plt.show()