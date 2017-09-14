# Code for problem 3

from math import exp, cos, sin
import matplotlib.pyplot as plt

def equation(x):
    return(1/(1+exp(-2*x))+cos(x))

def derivative(x):
    return((2*exp(2*x))/((exp(2*x)+1)**2)-sin(x))

# Finding the first root

root1=-2.0
iteration1=0

while abs(root1+1.6092791) >= 10**(-7):
    root1=root1-equation(root1)/derivative(root1)
    iteration1=iteration1+1


# Finding the second root

root2=3.0
iteration2=0

while abs(root2-3.0764211) >= 10**(-7):
    root2=root2-equation(root2)/derivative(root2)
    iteration2=iteration2+1

# Finding two smallest roots

[ [root1,iteration1],[root2,iteration2] ]

def rightside(x):
    return -cos(x)
def leftside(x):
    return 1/(1+exp(-2*x))

a = -3
b = 12.0
split = 1000.0

step = (b-a)/1000
X = list(); leftY = list(); rightY = list()
for i in range(int( (b-a)/step) ):
    x = a + i*step;
    leftY.append( leftside(x) )
    rightY.append(rightside(x))
    X.append(x)
    
plt.title("Problem 3")
plt.plot( X, leftY, color = "purple", label = "1/[1+exponent(-2*x)]" )
plt.plot( X, rightY, color = "red", label = "-cos(x)" )
plt.legend(loc = "lower right")
plt.xlim([a, b])
plt.ylim([-1.5, 2.0])
plt.show()


