# -*- coding: utf-8 -*-
#######  START Administrivia 
m400group =  7  # change this to your group number

m400names = ['Albert Que', 'Yefa Qi', 'Sylvia Isela Ramirez'] # change this for your names

def printNames():
        print("3-Linear_Interpolation-Group_7.py for group %s:\n"%(m400group)),
        for name in m400names:
            print("%s, "%(name)),
        print

printNames()

#######  END Administrivia

import matplotlib.pyplot as plt                             # plotting 
from math import *                                          # 'e' and trig fun's
from numpy import arange                                    # arange

def zeroV(m):
    z = [0]*m
    return z

# GLOBAL DATA
x_vals = [0, 1./6, 1./3, 1./2, 7./12, 2./3, 3./4, 5./6, 11./12, 1]

x_domain = arange(0,2, 1e-2)

fx = zeroV(10)

dfx = zeroV(10)

def sine_func(x):
    return(1.6*e**(-2*x)*sin(3*pi*x))

def sine_deriv(x):
    return((1.6)*(e**(-2*x))*(cos(3*pi*x))*(3*pi) + (1.6)*(-2)*(e**(-2*x))*(sin(3*pi*x)))

def runCalcs():
    "Find values for f(x) and f'(x)"
    for i in range(len(x_vals)):
        fx[i] += sine_func(x_vals[i])
        dfx[i] += sine_deriv(x_vals[i])

def showData():
    "Displays calculated values of f(x) and f'(x)"
    print("")
    for x in range(len(fx)):
        print("The value of f(" + str(x_vals[x]) + ") is: " + str(fx[x]))
    print("")
    for x in range(len(dfx)):
        print("The value of f'(" + str(x_vals[x]) + ") is: " + str(dfx[x]))

runCalcs()
showData()

# END TEST DATA

# Construct linear splines, and return range value.
def lin_int(x1, x2, y1, y2, x):
    """ lin_int(x1, x2, y1, y2, x) takes as input data pts x1, x2, y1, y2 and constructs
        corresponding linear spine polynomials and also takes a domain element x and returns
        a range element y to be graphed."""

    new_y = y1 + ((y2 - y1)/(x2 - x1))*(x - x1)
    new_y1 = ((y2 - y1)/(x2 - x1))*x + ((y1*x2 - y2*x1)/(x2 - x1))
    return(new_y)

# Set up and construct domain and range data for linear spline interpolant.
lin_ys = []
lin_domain = []

s = 0

# Computes the range in a piece-wise fashion, between two data points,
# x[i] and x[i+1].
for i in range(len(x_vals)-1):
    # create steps 1/10 of the distance between two points.
    h = (x_vals[i + 1] - x_vals[i])
    step = h / 10
    # calculate the appropriate range values between knots.
    while (s < x_vals[i + 1]):
        lin_ys.append(lin_int(x_vals[i], x_vals[i + 1], fx[i], fx[i+1], s))
        lin_domain.append(s)
        s = s + step

# Test data for sin_ys
sin_ys = [sine_func(x) for x in x_domain]

# Plot the linear interpolant, the x_vals and corresponding y_vals of the 
# given data.
plt.title("Linear Interpolation")                     
plt.ylabel("Y-Axis")                                    
plt.xlabel("X-Axis")   
plt.axis([0, 1.1, -1, 1.5], 'equal')
plt.axhline(y=0, color='gray')
plt.axvline(x=0, color='gray')

plt.plot(x_vals, fx, 'ro')
plt.plot(x_domain, sin_ys, 'blue', label= '$f(x)$')
plt.plot(lin_domain, lin_ys, 'green', label= '$Linear(x)$')

plt.legend(loc='lower right')

plt.show()
