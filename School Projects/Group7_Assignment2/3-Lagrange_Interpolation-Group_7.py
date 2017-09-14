# -*- coding: utf-8 -*-
#######  START Administrivia 
m400group =  7  # change this to your group number

m400names = ['Albert Que', 'Yefa Qi', 'Sylvia Isela Ramirez'] # change this for your names

def printNames():
        print("3-Lagrange_Interpolation-Group_7.py for group %s:\n"%(m400group)),
        for name in m400names:
            print("%s, "%(name)),
        print

printNames()

#######  END Administrivia

import matplotlib.pyplot as plt                             # plotting 
from math import *                                          # 'e' and trig fun's
from numpy import arange                                    # arange

# GLOBAL DATA

nodes = [0.0, 1.0/6, 1.0/3, 1.0/2, 7.0/12, 2.0/3, 3.0/4, 5.0/6, 11.0/12, 1.0]    # list of nodes for x values for LaGrange

numOfNodes = len(nodes)                                     

funVals = [0 for i in range(numOfNodes)]                    # list for calculated results of f(x)

derivVals = [0 for i in range(numOfNodes)]                  # list for calculated results for f'(x)

fPlotVals = []                                              # empty list will be populated with various f(x) vals

lagrangePlotVals = []                                       # empty list will be populated with various P(x) vals

errorPlotVals = []                                          # empty list will contain errors of each P(x)

domain = arange(0,1.1, 0.01)                                # arange() shows start, stop, and step
                                                            
numOfPlotPoints = len(domain)                               
                    


# FUNCTIONS

def calculateFun(x):
    "Equation for the calculation of f(x)=1.6e^(-2x)sin(3πx)"
    return(1.6*e**(-2*x)*sin(3*pi*x))


def calculateDeriv(x):
    "Equation for the calculation of f'(x)=1.6e^(-2x)[3π(cos(3πx))-2(sin(3πx))]"
    return(1.6*e**(-2*x)*((3*pi)*(cos(3*pi*x))-(2)*(sin(3*pi*x))))           

def runCalcs():
    "Find values for f(x) and f'(x)"
    for x in range(numOfNodes):                     
        funVals[x] += calculateFun(nodes[x])        
        derivVals[x] += calculateDeriv(nodes[x])    

def calcLagrange(x, nodes, funVals):
    "Takes as input an x value for each step in the domain, the node values, and the values of f(x) at each node to create the approximation of P(x).  Returns P(specific step)."
    pOfX = 0.0                                      # initialize P(x)
    for i in range(numOfNodes):                     # for each node
        L = 1.0                                     # initialize L(x) to be 1, as given in Problem 1
        for k in range(numOfNodes):                 # compute L(x) and multiply by old value
            if i != k:                              # make sure xi is not part of calculation
                L = L * (x - nodes[k]) / (nodes[i] - nodes[k])  
                                                                
        pOfX = pOfX + funVals[i] * L                # update our P(x) with L(x) for each node
    return(pOfX)                                    # P(x) is returned

def getPlotPoints():
    "Finds the y values for each step in domain of f(x), P(x), and E(x)"
    for x in domain:                                       
        lagrangePlotVals.append(calcLagrange(x, nodes, funVals))    # calculate P(x)
        fPlotVals.append(calculateFun(x))                           # calculate f(x)

    for i in range(numOfPlotPoints):                       
        errorPlotVals.append(abs(fPlotVals[i] - lagrangePlotVals[i]))   # take difference between two plots, E(x)
                                                                       
def plotLagrange():
    plt.title("Lagrange Interpolation")                     
    plt.ylabel("Y-Axis")                                    
    plt.xlabel("X-Axis")                                    
    plt.axis([-.05, 1.05, -.75, 1.25])                      # set boundaries (xmin, xmax, ymin, ymax)
    plt.axhline(y=0, color='gray')                          
    plt.axvline(x=0, color='gray')                          

    plt.plot(nodes, funVals, 'ro')                          # plot a red circle at each (x,f(x)) for nodes
    plt.plot(domain, fPlotVals, color='blue', label= '$f(x)$')               # plot f(x) at each x-step in domain
    plt.plot(domain, lagrangePlotVals, color='purple', label= '$L(x)$')      # plot P(x)
    plt.plot(domain, errorPlotVals, color='red', label= '$E(x)$')            # show a plot of E(x) values across the domain
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
        
def num_three_lagrange():
    runCalcs()                                                  # compute f(x) and f'(x)
    getPlotPoints()                                             # calculate plot points
    showData()                                                  # output f(x) and f'(x)
    plotLagrange()                                              # draw our plot

num_three_lagrange()
