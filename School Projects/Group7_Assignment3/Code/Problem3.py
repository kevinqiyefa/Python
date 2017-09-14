
from math import e

######################################################
# Problem #3
######################################################

# takes a final power n
# returns a list with values 10^-1, 10^-2, ... , 10^-n
def createH(n):
    i = 1
    h = []
    
    if(n <= 0):
        print "Error: power input invalid.\n"
        return -1
    else:
        while(i <= n):
            h.append(10**-i)
            i += 1
        return h

# returns value of e^(-x^2/2) using the parameter of x
def g(x):
    return e**(-1*x**2/2)

# returns an estimate to g'(x) using x and h
def centralDifference(x,h):
    return (g(x+h) - g(x-h)) / (2*h)

# returns the exact value of the f'(x) at x
def exact(x):
    return -1 * x * e**(-1*x**2/2)

# returns error = exact - estimate
def relativeError(x,d):
    return exact(x) - d

######################################################
# test code
######################################################

# creates a list of h values
h = createH(20)

# d will store estimates of g'(x) using the central difference formula
d = []

# r will store relative errors for each value of h
r = []



# calculates estimates of g'(x) from the central difference formula and relative errors
x = 1.4
i = 0

while(i < 20):
    d.append(centralDifference(x, h[i]))
    r.append(relativeError(x, d[i]))
    i += 1

print "The table of estimates of g'(1.4) :\n", d
print "\nThe relative errors of each estimates:\n", r

