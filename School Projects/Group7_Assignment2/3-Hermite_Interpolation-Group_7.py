# -*- coding: utf-8 -*-
#######  START Administrivia 
m400group =  7  # change this to your group number

m400names = ['Albert Que', 'Yefa Qi', 'Sylvia Isela Ramirez'] # change this for your names

def printNames():
        print("3-Hermite_Interpolation-Group_7.py for group %s:\n"%(m400group)),
        for name in m400names:
            print("%s, "%(name)),
        print

printNames()

#######  END Administrivia

from pylab import *
from math import e
from math import sin
from math import cos
from math import pi
from numpy import arange

def zero(m,n):
    "Create zero matrix"
    new_mat = [[0 for col in range(n)] for row in range(m)]
    return new_mat

def zeroV(m):
    v = [0]*m
    return(v)
                                                                                                                                                                    
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
    fx[i] = sine_func(x_vals[i])
    dfx[i] = sine_deriv(x_vals[i])

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

def hermite(x, x_pts, fx, dfx):
    """Takes as input domain elements x, and test data: x_pts, fx, dfx 
       Computes the coefficients of the Hermite interpolating polynomial
       Calculates the range values, and graphs."""

    # Sets up and stores the elements of a divided difference table into a matrix Q.  The elements at Qii are the coefficients of the polynomial.
    n = len(x_pts)
    Q = zero(2*n, 2*n)
    Qii = []
    
    # zs account for first derivative
    z = getZ(x_pts)
    for i in range(n):
        Q[2*i][0] = fx[i]
        Q[2*i + 1][0] = fx[i]
        Q[2*i + 1][1] = dfx[i]
        if i != 0.: 
            Q[2*i][1] = (Q[2*i][0] - Q[2*i - 1][0]) / (z[2*i] - z[2*i - 1])
    for i in range(2, 2*n):
        for j in range(2, i+1):
            Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (z[i] - z[i - j])
    # Populate the array Qii with the values along the diagonal of Q, the coefficients.
    for i in range(0, 2*n):
        Qii.append(Q[i][i])
    # Compute and return the value of H(x) for graphing
    Hx = computePx(x, z, Qii)
    return(Hx)

def getZ(x_pts):
    """Constructs a vector z in the appropriate form to be used in the divided difference table."""
    n = len(x_pts)
    z_ = zeroV(2*n)
    for i in range(len(x_pts)):
        z_[2*i] += x_pts[i]
        z_[2*i + 1] += x_pts[i]
    return(z_)

def computePx(x, z, Q):
    """computePx(x, z, Q) takes as input a domain element x, a vector z,and the coefficients in 
       Q of the Hermite polynomial, and constructs and computes H(x), returning range values """
    d = zeroV(len(z))
    for i in range(len(d)):
        d[i] = x - z[i]
    n = len(d)    
    np = []
    prod = 1.
    for i in range(0, n-1):
        for j in range(0, i):
           prod *= d[j]
        prod *= d[i]
        np.append(prod)
        prod = 1.
    # compute sum of Q's and x-z[i's]
    sum = Q[0]
    for i in range(1, len(Q)):
        sum += Q[i]*np[i-1]
    return(sum)
    
# Sets up range values
hermite_ys = [hermite(x, x_vals, fx, dfx) for x in x_domain]
sin_ys = [sine_func(x) for x in x_domain]

# Sets up plots.
ax = subplot(111)
subplots_adjust(left=0.25, bottom=0.25)
matplotlib.pyplot.title("Hermite Interpolation")

a0 = 0

p, = plot(x_domain, sin_ys, color='blue', label= '$f(x)$')
l, = plot(x_domain, hermite_ys, color='green', label= '$L(x)$')
k, = plot(x_vals, fx, 'ro')

plt.legend(loc='lower right')


axis([0, 1.1, -1, 1.5])
axhline(linewidth=.5, color='grey')

show()
