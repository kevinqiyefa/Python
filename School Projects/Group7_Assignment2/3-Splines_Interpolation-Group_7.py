# -*- coding: utf-8 -*-
#######  START Administrivia 
m400group = 7   # change this to your group number

m400names = ['Albert Que', 'Yefa Qi', 'Sylvia Isela Ramirez'] # change this for your names

def printNames():
    print("3-Splines_Interpolation-Group_7.py for group %s:\n"%(m400group)),
    for name in m400names:
        print("%s, "%(name)),
    print

printNames()

#######  END Administrivia

import matplotlib.pyplot as plt                             # plotting 
from math import *                                          # 'e' and trig fun's
from numpy import arange                                    # arange

# GLOBAL DATA

nodes = [0.0, 1.0/6, 1.0/3, 1.0/2, 7.0/12, 2.0/3, 3.0/4, 5.0/6, 11.0/12, 1.0]    # list of nodes for x values

numOfNodes = len(nodes)                                     

funVals = [0 for i in range(numOfNodes)]                    # list for calculated results for f(x)
                                                           
derivVals = [0 for i in range(numOfNodes)]                  # list for calculated results for f'(x)
                                                          
fPlotVals = []                                              # empty list will be populated with various f(x) vals

linSplinePlotXVals = []                                     # empty list will be populated with spline x-values
linSplinePlotYVals = []                                     # empty list will be populated with spline y-values

domain = arange(0,1.1, 0.01)                                # arange() start, stop(non-inclusive), step
                                                            
numOfPlotPoints = len(domain)                               # number of plot points in domain

# FUNCTIONS

def calculateFun(x):
    "Equation for the calculation of f(x)=1.6e^(-2x)sin(3πx)"
    return(1.6*e**(-2*x)*sin(3*pi*x))


def calculateDeriv(x):
    "Equation for the calculation of f'(x)=1.6e^(-2x)[3π(cos(3πx))-2(sin(3πx))]"
    return(1.6*e**(-2*x)*((3*pi)*(cos(3*pi*x))-(2)*(sin(3*pi*x))))           

def runCalcs():
    "Function to fill lists with calculated values for f(x) and f'(x)"
    for x in range(numOfNodes):                            # calculate f(x) and f'(x)
        funVals[x] += calculateFun(nodes[x])                    
        derivVals[x] += calculateDeriv(nodes[x])
        
def calcLinSpline(x, x1, y, y1, cur_x):
    """The calcLinSpline function will take as input a beginning and ending value for x (i.e. x, x1), as well as
    a beginning and ending value for y=f(x) (i.e. y, y1), the four of which represent the location of two nodes
    from our list of nodes, moving from left to right.  It must also accept the curent x-value at which the spline
    is currently being calculated somewhere in the domain of f(x).  Return value is y-value of point in range of
    spline of f(x)."""  
    splineVal = y + (cur_x-x)*((y1-y)/(x1-x))               # basically point slope formula (y = b, m = slope
                                                            # calculated by (y2-y1/x2-x1), and x = cur_x-x
    return(splineVal)

def getPlotPoints():
    "The getPlotPoints function will find the y values for each step in domain of f(x) and linear spline"
    for x in domain:                                        
        fPlotVals.append(calculateFun(x))                        # calculate f(x) plot points
    atX = nodes[0]                                          
    stepsize = 0.001                                       
                                                            # important to note that too large a value will
                                                            # result in a loss of precision in approximation
                                                            # and strange spline behavior near nodes
    for i in range(numOfNodes-1):                           
        while(atX <= nodes[i+1]):                           # for each node,
            linSplinePlotXVals.append(atX)                  # add current x value to list of spline x vals
            linSplinePlotYVals.append(calcLinSpline(nodes[i],
                nodes[i+1], funVals[i], funVals[i+1], atX)) # add calculated y value to list of spline y vals
            atX += stepsize                                 # increment plot location slightly and recalc

def plotLinSpline():
    plt.title("Spline Interpolation")             
    plt.ylabel("Y-Axis")                                   
    plt.xlabel("X-Axis")                                    
    plt.axis([-.05, 1.05, -.75, 1.25])                      # set boundaries (xmin, xmax, ymin, ymax)
    plt.axhline(y=0, color='gray')                         
    plt.axvline(x=0, color='gray')                          

    plt.plot(nodes, funVals, 'ro')                          # plot a red circle at each (x,f(x)) for nodes
    plt.plot(domain, fPlotVals, color='blue', label= '$f(x)$')               # plot f(x) at each x-step in domain
    plt.plot(linSplinePlotXVals, linSplinePlotYVals, color='purple', label= '$Splines(x)$')      # plot splines

    plt.legend(loc='lower right')
    
    plt.show()                                              

def showData():
    "Displays calculated values of f(x) and f'(x)"
    print("")
    for x in range(len(funVals)):
        print("The value of f(" + str(nodes[x]) + ") is: " + str(funVals[x]))
    print("")
    for x in range(len(derivVals)):
        print("The value of f'(" + str(nodes[x]) + ") is: " + str(derivVals[x]))

def num_three_splines():
    runCalcs()                                                  
    getPlotPoints()                                             # calculate plot points
    showData()                                                  # output f(x) and f'(x)
    plotLinSpline()                                             # draw plot

num_three_splines()
