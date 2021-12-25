#Modified Euler's Method or Predictor-Corrector Method

import math as m
import numpy as np

#Initial Conditions and step
x0,y0,h = 1,2,0.2
y = y0
x = 5.2 # the x-value in which we want y
n = 3 # number of times we want the y value to be modified
X = []
Y = []

def f(x,y):
    a = m.log((x+y),m.e)
    return a

for i in np.arange(x0,x+h,h):
    X.append(i)
    y_n = y
    Y.append(y_n)
    y += h*f(i,y)
    for j in range(n):
        y = y_n + (h/2)*(f(i,y_n)+f(i+h,y))
        
# to print the solution
print('The x co-ordinates :    ',X)
print('Corresponding y values :',Y)

# for plotting
import matplotlib.pyplot as plt
plt.plot(X,Y)
plt.show()
        