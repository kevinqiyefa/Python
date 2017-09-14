######################################
############  Problem 2  #############
######################################

from math import *
import matplotlib.pyplot as plt

def f(t):
    return cos(2*pi*t)

def f2(x):
    return -4 * pi**2 * x        

# Problem 2 Euler's Method
def euler2(t,x,x1,h,n):

    sol = [x]
    
    while(t < n):
        temp = x
        x  += h * x1
        x1 += h * f2(temp)
        t += h
        sol.append(x)
  
    return sol
 

def errorList(h,list):
    e = []
    i = 0
    for x in list:
        e.append(abs((f(i) - x) / f(i)))
        i += h  
    return e
          
          
def populateT(h,n):
    t = 0
    s = [t]  
    while(t < n):
        t += h
        s.append(t)
    return s
          
### print output as a List ####
def printList(h,list,errors):
    print "t\tExact Solution\t\tx\t\tRelative Error"    
    step = 0
    for i in range(len(list)):
        print step, "\t", f(step), "\t\t", list[i] , "\t\t", errors[i]
        step += h
        
    
#################################
############  Test  #############
#################################  
                      
t = 0
x = 1.0
x1 = 0.0
h = 0.2
n = 1.2
      

print
print "Solutions for Problem 2:"

print "P2-Euler's Method, Step size (h = 0.2):"
printList(h,euler2(t,x,x1,h,n),errorList(h,euler2(t,x,x1,h,n)))
print "\nP2-Euler's Method, Step size (h = 0.1):"
printList(h/2,euler2(t,x,x1,h/2,n),errorList(h/2,euler2(t,x,x1,h/2,n)))
print "\nP2-Euler's Method, Step size (h = 0.05):"
printList(h/4,euler2(t,x,x1,h/4,n),errorList(h/4,euler2(t,x,x1,h/4,n)))

'''
###### ploting Euler's Method
plt.plot(populateT(h,n),euler2(t,x,x1,h,n), label="Step size 0.2", color = "blue")
plt.plot(populateT(h/2,n),euler2(t,x,x1,h/2,n), label="Step size 0.1", color = "green")
plt.plot(populateT(h/4,n),euler2(t,x,x1,h/4,n), label="Step size 0.05", color = "red")
plt.title("P2-Euler's Method")
plt.axis([0,1.2,-12,10])
plt.legend(loc = 4)
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()
'''
# plotting P2-Euler's Method relative error
plt.plot(populateT(h,n),errorList(h,euler2(t,x,x1,h,n)), label="Step size 0.2", color = "blue")
plt.plot(populateT(h/2,n),errorList(h/2,euler2(t,x,x1,h/2,n)), label="Step size 0.1", color = "green")
plt.plot(populateT(h/4,n),errorList(h/4,euler2(t,x,x1,h/4,n)), label="Step size 0.05", color = "red")
plt.title("Relative Error - P2-Euler's Method")
plt.axis([0,1.2,0,20])
plt.legend(loc = "upper left")
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show()
