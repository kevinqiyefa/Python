######################################
############  Problem 1  #############
######################################  

from math import *
import matplotlib.pyplot as plt 

def f(t):
    return (1.25)*e**(-2*t) + (0.25)*(2*t-1)
    
def f1(t,x):
    return t - (2*x)    

######   Euler's Method ####### 
def euler(t,x,h,n):

    s = []   
    s.append(x)
    while(t < n):
        x += h * f1(t,x)
        t += h
        s.append(x)

    return s
    
######   Modified Euler's Method #######    
def modifiedEuler(t,x,h,n):

    s = [x] 
    while(t < n):
        f = f1(t,x)
        t += h
        x += (0.5)*h * (f + f1(t, x + h*f))
        s.append(x)
    return s

# 4th order Runge-Kutta method
def rungeKutta(t,x,h,n):

    s = [x]
    
    while(t < n):
        k1 = f1(t,x)
        k2 = f1(t + 0.5*h, x + 0.5*k1*h)
        k3 = f1(t + 0.5*h, x + 0.5*k2*h)
        k4 = f1(t + h, x + k3*h)
        x += h * (k1 + 2*k2 + 2*k3 + k4)/6
        t += h
        s.append(x)

    return s
   
#### function for graph ###            
def populateT(h,n):
    t = 0
    sol = [t]
    
    while(t < n):
        t += h
        sol.append(t)
    return sol
    
def errorList(h,list):
    er = []
    i = 0
    for x in list:
        er.append(abs((f(i) - x) / f(i)))
        i += h    
    return er

#### print output in list #####        
def printList(h,list,errors):
    print "t\tx\t\tExact Solution\t\tRelative Error"    
    s = 0
    for i in range(len(list)):
        print s, "\t", list[i], "\t\t", f(s), "\t\t", errors[i]
        s += h

        
#################################
############  Test  #############
#################################                        
t = 0
x = 1.0
h = 0.2
      

print
print "Solutions for Problem 1:"


#################### Output for Euler's Method #################################

print "Euler's Method, Step size (h = 0.2):"
printList(h,euler(t,x,h,1.8),errorList(h,euler(t,x,h,1.8)))

print
print "Euler's Method, Step size (h = 0.1):"
printList(h/2,euler(t,x,h/2,2),errorList(h/2,euler(t,x,h/2,2)))

print
print "Euler's Method, Step size (h = 0.05):"
printList(h/4,euler(t,x,h/4,2),errorList(h/4,euler(t,x,h/4,2)))

###### ploting Euler's Method
plt.plot(populateT(h,1.8),euler(t,x,h,1.8), label="Step size 0.2", color = "blue")
plt.plot(populateT(h/2,2),euler(t,x,h/2,2), label="Step size 0.1", color = "green")
plt.plot(populateT(h/4,2),euler(t,x,h/4,2), label="Step size 0.05", color = "red")
plt.title("Euler's Method")
plt.axis([0,2,0,1])
plt.legend(loc = 4)
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()

# plotting Euler's Method relative error
plt.plot(populateT(h,1.8),errorList(h,euler(t,x,h,1.8)), label="Step size 0.2", color = "blue")
plt.plot(populateT(h/2,2),errorList(h/2,euler(t,x,h/2,2)), label="Step size 0.1", color = "green")
plt.plot(populateT(h/4,2),errorList(h/4,euler(t,x,h/4,2)), label="Step size 0.05", color = "red")
plt.title("Relative Error - Euler's Method")
plt.axis([0,2,0,0.25])
plt.legend(loc = "upper right")
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()


################# Output for Modiefied Euler's Method ##########################

print
print "\nModified Euler's Method, Step size (h = 0.2):"
printList(h,modifiedEuler(t,x,h,1.8),errorList(h,modifiedEuler(t,x,h,1.8)))
print "\nModified Euler's Method, Step size (h = 0.1):"
printList(h/2,modifiedEuler(t,x,h/2,2),errorList(h/2,modifiedEuler(t,x,h/2,2)))
print "\n\nModified Euler's Method, Step size (h = 0.05):"
printList(h/4,modifiedEuler(t,x,h/4,2),errorList(h/4,modifiedEuler(t,x,h/4,2)))

# plotting Modified Euler's Method
plt.plot(populateT(h,1.8),modifiedEuler(t,x,h,1.8), label="Step size 0.2", color = "blue")
plt.plot(populateT(h/2,2),modifiedEuler(t,x,h/2,2), label="Step size 0.1", color = "green")
plt.plot(populateT(h/4,2),modifiedEuler(t,x,h/4,2), label="Step size 0.05", color = "red")
plt.title("Modified Euler's Method")
plt.axis([0,2,0,1])
plt.legend(loc = 4)
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()

# plotting Modified Euler's Method relative error
plt.plot(populateT(h,1.8),errorList(h,modifiedEuler(t,x,h,1.8)), label="Step size 0.2", color = "blue")
plt.plot(populateT(h/2,2),errorList(h/2,modifiedEuler(t,x,h/2,2)), label="Step size 0.1", color = "green")
plt.plot(populateT(h/4,2),errorList(h/4,modifiedEuler(t,x,h/4,2)), label="Step size 0.05", color = "red")
plt.title("Relative Error - Modified Euler's Method")
plt.axis([0,2,0,0.04])
plt.legend(loc = "upper right")
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()


################# Output for 4th order Runge-Kutta Method #######################

print "\n\n4th order Runge-Kutta Method, Step size (h=0.2):"
printList(h,rungeKutta(t,x,h,1.8),errorList(h,rungeKutta(t,x,h,1.8)))
print "\n4th order Runge-Kutta Method, Step size (h=0.1):"
printList(h/2,rungeKutta(t,x,h/2,2),errorList(h/2,rungeKutta(t,x,h/2,2)))
print "\n4th order Runge-Kutta Method, Step size (h=0.05):"
printList(h/4,rungeKutta(t,x,h/4,2),errorList(h/4,rungeKutta(t,x,h/4,2)))

# plotting 4th order Runge-Kutta Method
plt.plot(populateT(h,1.8),rungeKutta(t,x,h,1.8), label="Step size 0.2", color = "blue")
plt.plot(populateT(h/2,2),rungeKutta(t,x,h/2,2), label="Step size 0.1", color = "green")
plt.plot(populateT(h/4,2),rungeKutta(t,x,h/4,2), label="Step size 0.05", color = "red")
plt.title("4th order Runge-Kutta Method")
plt.axis([0,2,0,1])
plt.legend(loc = 4)
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()


# plotting 4th order Runge-Kutta Method relative error
plt.plot(populateT(h,1.8),errorList(h,rungeKutta(t,x,h,1.8)), label="Step size 0.2", color = "blue")
plt.plot(populateT(h/2,2),errorList(h/2,rungeKutta(t,x,h/2,2)), label="Step size 0.1", color = "green")
plt.plot(populateT(h/4,2),errorList(h/4,rungeKutta(t,x,h/4,2)), label="Step size 0.05", color = "red")
plt.title("Relative Error - 4th order Runge-Kutta")
plt.axis([0,2,0,0.00035])
plt.legend(loc = "upper right")
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()