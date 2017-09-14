import math
import copy
############################################################
# problem 2(a)
############################################################
pi = 3.14159265359

print "\n(a)"
a = 0.0
b = 0.5

correct_answer = 0.318309886183791

def a_eval_y_points(X):
    Y = list()
    for i in range( len(X) ):
        y = math.sin( pi * X[i])
        Y.append(y)
    return Y


def a_divide_x(n, a, b):
    X = list()
    X.append(a)
    d = (b-a)/(n-1)
    for i in range(1, n-2):
        X.append(X[0] + d*i)
    X.append(b)
    return X
    
def a_trap(X, Y):
    total = 0
    Y = a_eval_y_points(X)
    for i in range(len(X)-1):
        d = X[i+1]-X[i]
        area = (Y[i+1]+Y[i])/2*d
        total+= area
    return total

def get_gauss_xws(n):
    gauss_xs = [
    [-0.5773502691896257, 0.5773502691896257],
    [-0.7745966692414834, 0.0000000000000000, 0.7745966692414834],
    [-0.3399810435848563, 0.3399810435848563, -0.8611363115940526, 	0.8611363115940526],
    [0.0000000000000000, -0.5384693101056831, 0.5384693101056831, -0.9061798459386640, 0.9061798459386640],
    [0.6612093864662645, -0.6612093864662645, -0.2386191860831969, 0.2386191860831969, -0.9324695142031521, 0.9324695142031521],
    [0.0000000000000000, 0.4058451513773972, -0.4058451513773972, -0.7415311855993945, 0.7415311855993945, -0.9491079123427585, 0.9491079123427585],
    [-0.1834346424956498, 0.1834346424956498, -0.5255324099163290, 0.5255324099163290, -0.7966664774136267, 0.7966664774136267, -0.9602898564975363, 0.9602898564975363],
    [0.0000000000000000, -0.8360311073266358, 0.8360311073266358, -0.9681602395076261, 0.9681602395076261, -0.3242534234038089, 0.3242534234038089, -0.6133714327005904, 0.6133714327005904]
    ]
    gauss_ws = [
    [1.0000000000000000, 1.0000000000000000],
    [0.5555555555555556, 0.8888888888888888, 0.5555555555555556],
    [0.6521451548625461, 0.6521451548625461, 0.3478548451374538, 0.3478548451374538],
    [0.5688888888888889, 0.4786286704993665, 0.4786286704993665, 0.2369268850561891, 0.2369268850561891],
    [0.3607615730481386, 0.3607615730481386, 0.4679139345726910, 0.4679139345726910, 0.1713244923791704, 0.1713244923791704],
    [0.4179591836734694, 0.3818300505051189, 0.3818300505051189, 0.2797053914892766, 0.2797053914892766, 0.1294849661688697, 0.1294849661688697],
    [0.3626837833783620, 0.3626837833783620, 0.3137066458778873, 0.3137066458778873, 0.2223810344533745, 0.2223810344533745, 0.1012285362903763, 0.1012285362903763],
    [0.3302393550012598, 0.1806481606948574, 0.1806481606948574, 0.0812743883615744, 0.0812743883615744, 0.3123470770400029, 0.3123470770400029, 0.2606106964029354, 0.2606106964029354]
    ]
    return gauss_xs[n-2], gauss_ws[n-2]
    
    
### Gaussian Quadrature ###
def convert_gauss_xs(X, a, b):
    for i in range(len(X)):
        X[i] = (b - a)/2*X[i] + (a+b)/2
    return X

def gauss_quad(X, Y, W, a, b):
    sum = 0
    for i in range(len(X)):
        sum+=(b-a)/2*W[i]*Y[i]
    return sum    
    
#### Trapezoidal #####
def divide_x(n, a, b):
    X = list()
    X.append(a)
    d = (b-a)/(n-1)
    for i in range(1, n-1):
        X.append(X[0] + d*i)
    X.append(b)
    return X  
    
    
### Romberg
def romberg(X, Y):
    n = len(X)
    j = 1
    roms = list()
    eval_x = [ X[0], X[len(X)-1] ]
    eval_y = [ Y[0], Y[len(Y)-1] ]
    roms.append( trap(eval_x, eval_y) )
    div = 2
    while (n-1)/div >= 1:
        eX = list()
        eY = list()
        interval = (n-1)/div
        #get points for trap rule
        k=0
        while interval*k < n:
            eX.append(X[interval*k])
            eY.append(Y[interval*k])
            k+=1 
        roms.append( trap(eX, eY) )
        div*=2

    level = 1
    while (len(roms) > 1):
        newRoms = list()
        for i in range(len(roms)-1):
            r = roms[i+1] + ( roms[i+1] - roms[i] )/( math.pow(2, 2*level)-1 )
            newRoms.append(r)
        roms = copy.copy(newRoms)
        level+=1
    return roms[0]    
    
### Trapezoid Rule
def trap(X, Y):
    total = 0
    #Y = a_eval_y_points(X)
    for i in range(len(X)-1):
        d = X[i+1]-X[i]
        area = (Y[i+1]+Y[i])/2*d
        total+= area
    return total
    
            
####################################################################
# Test and output    
###################################################################
print "\nGauss Quadrature:"
for i in range(2, 8):
    gp = get_gauss_xws(i)
    X = convert_gauss_xs(gp[0], a, b)
    Y = a_eval_y_points(X)
    W = gp[1]
    result = gauss_quad(X, Y, W, a, b)
    print "Result: " + str(result)
    if ( abs(result-correct_answer) < 0.0000001 ):
        print "Success at n = " + repr(i)
        print "Error = " + str(abs(result-correct_answer))
        break
    else:
        print "Failed at n = " + repr(i)
        print "E = " + str(abs(result-correct_answer))
        continue

print "\nTrapezoid Rule"
for i in range(800, 1000):
    X = divide_x(i, a, b)  
    Y = a_eval_y_points(X)
    result = a_trap(X, Y)
    if ( abs(result-correct_answer) < 0.0000001 ):
        print "Success at n = " + repr(i)
        print "Error = " + str(abs(result-correct_answer))
        break
    else:
        print "Failed at n = " + repr(i)
        print "E = " + str(abs(result-correct_answer))
        continue

#romberg
print "\nRomberg:"
for i in range(1, 30):
    n = 2**i+1
    X = divide_x(n, a, b)
    Y = a_eval_y_points(X)
    result = romberg(X, Y)
    print "Result: " + str(result)
    if ( abs(result-correct_answer) < 0.0000001 ):
        print "Success at n = " + repr(2**i+1)
        print "Error = " + str(abs(result-correct_answer))
        break
    else:
        print "Failed at n = " + repr(i)
        print "E = " + str(abs(result-correct_answer))
        continue