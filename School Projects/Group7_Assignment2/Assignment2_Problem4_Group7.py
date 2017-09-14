"""
Albert Que, Yefa Qi, Sylvia Isela Ramirez

Math 400, Assignment #2 Problem 04

Dr. David Sklar


Graphs L(9, 6) and PI(x)

"""

import matplotlib.pyplot as plt
from numpy import poly1d, arange

x_vals = [0, 1./6, 1./3, 1./2, 7./12, 2./3, 3./4, 5./6, 11./12, 1]

zeroVec = [0]*10

# Function for computing PI(x)
def pi_x(xn, x):
    px = 1.0
    for i in range(len(xn)):
        px *= (x - xn[i])
    return(px)

# Computes L(9, 6)
def lagrange(x_vals, x):
    Lx = 1.0
    for j in range(len(x_vals)):
        if j != 6:
            Lx = Lx * (x - x_vals[j]) / (x_vals[6] - x_vals[j]) 
    return(Lx)

# Graph the two plots
def graph(x_vals):
    
    x_domain = arange(-2, 2, 1e-2)    
    pxn = []
    lagrange_ys = [lagrange(x_vals, x) for x in x_domain]
    
    for i in range(len(x_domain)):
        pxn.append(pi_x(x_vals, x_domain[i]))

    plt.plot(x_domain, pxn, color='green')
    plt.plot(x_domain, lagrange_ys, color='blue')
    plt.plot(x_vals, zeroVec, 'ro')

    #make horizonal axis run from -pi to 2*pi while vertical axis goes from -2 to 2

    plt.axis([-1, 2, -3, 5], 'equal')

    #put horizontal and vertical lines because matplotlib puts axes around plot
    
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    #save plot to a file or show plot from IDLE shell

    plt.show()

graph(x_vals)
