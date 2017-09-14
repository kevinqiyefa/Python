import math
from math import *
import matplotlib.pyplot as plt



def rows(mat):
#   "return number of rows"
    return(len(mat))

def cols(mat):
#    "return number of cols"
    return(len(mat[0]))
 
def zero(m,n):
#    "Create zero matrix"
    new_mat = [[0 for col in range(n)] for row in range(m)]
    return new_mat
 
def transpose(mat):
#    "return transpose of mat"
    new_mat = zero(cols(mat),rows(mat))
    for row in range(rows(mat)):
        for col in range(cols(mat)):
            new_mat[col][row] = mat[row][col]
    return(new_mat)

def dot(A,B):
#    "vector dot product"
    if len(A) != len(B):
        print("dot: list lengths do not match")
        return()
    dot=0
    for i in range(len(A)):
        dot = dot + A[i]*B[i]
    return(dot)

def getCol(mat, col):
#    "return column col from matrix mat"
    return([r[col] for r in mat])

def getRow(mat, row):
#    "return row row from matrix mat"
    return(mat[row])

def matMult(mat1,mat2):
#    "multiply two matrices"
    if cols(mat1) != rows(mat2):
        print("matMult: mismatched matrices")
        return()
    prod = zero(rows(mat1),cols(mat2))
    for row in range(rows(mat1)):
        for col in range(cols(mat2)):
            prod[row][col] = dot(mat1[row],getCol(mat2,col))
    return(prod)

def vec2rowVec(vec):
#    "[a,b,c] -> [[a,b,c]]"
    return([vec])

def vec2colVec(vec):
    return(transpose(vec2rowVec(vec)))

def colVec2vec(mat):
    rowVec = transpose(mat)
    return(rowVec[0])

def augment(mat,vec):
#    "given nxn mat and n length vector return augmented matrix"
    amat = []
    for row in range(rows(mat)):
        amat.append(mat[row]+[vec[row]])
    return(amat)

def vectorQ(V):
#    "mild test to see if V is a vector"
    if type(V) != type([1]):
        return(False)
    if type(V[0]) == type([1]):
        return(False)
    return(True)

def scalarMult(a,mat):
#    "multiply a scalar times a matrix"
    if vectorQ(mat):
        return([a*m for m in mat])
    for row in range(rows(mat)):
        for col in range(cols(mat)):
            mat[row][col] = a*mat[row][col]
    return(mat)

def addVectors(A,B):
 #   "add two vectors"
    if len(A) != len(B):
        print("addVectors: different lengths")
        return()
    return([A[i]+B[i] for i in range(len(A))])

def swaprows(M,i,j):
#    "swap rows i and j in matrix M"
    N=copyMatrix(M)
    T = N[i]
    N[i] = N[j]
    N[j] = T
    return N

def copyMatrix(M):
    return([[M[row][col] for col in range(cols(M))]for row in
            range(rows(M))])

def addrows(M, f, t, scale=1):
#    "add scale times row f to row t"
    N=copyMatrix(M)
    T=addVectors(scalarMult(scale,N[f]),N[t])
    N[t]=T
    return(N)
    
def show(mat):
#    "Print out matrix"
    for row in mat:
        print(row)


### The naive gaussian elimination code begins here.

def findPivotrow1(mat,col):
#    Finds index of the first row with nonzero entry on or
#    below diagonal.  If there isn't one return(-1).

    epsilon = 10**(-17)
    for row in range(col, rows(mat)):
#        if mat[row][col] != 0:
        if abs(mat[row][col]) > epsilon:
            return(row)
    return(-1)


def rowReduce(M):
#    return row reduced version of M

    N = copyMatrix(M)
    cs = cols(M)-2   # no need to consider last two cols
    rs = rows(M)
    for col in range(cs+1):
        j = findPivotrow1(N,col)
        if j < 0:
            print("\nrowReduce: No pivot found for column index %d "%(col))
            return(N)
        else:
            if j != col:
                N = swaprows(N,col,j)
            scale = -1.0 / N[col][col]
            for row in range(col+1,rs):                
                N=addrows(N, col, row, scale * N[row][col])
    return(N)


def backSub(M):

#   given a row reduced augmented matrix with nonzero 
#   diagonal entries, returns a solution vector
    

    cs = cols(M)-1 # cols not counting augmented col
    sol = [0 for i in range(cs)] # place for solution vector
    for i in range(1,cs+1):
        row = cs-i # work backwards
        sol[row] = ((M[row][cs] - sum([M[row][j]*sol[j] for
                    j in range(row+1,cs)])) / M[row][row]) 
    return(sol)


def diag_test(mat):

#   Returns True if no diagonal element is zero, False
#   otherwise.
    

    for row in range(rows(mat)):
        if mat[row][row] == 0:
            return(False)
    else:
        return(True)


def ge_1(aug):    

#   Given an augmented matrix it returns a list.  The [0]
#   element is the row-reduced augmented matrix, and 
#   ge_1(aug)[1] is a solution vector.  The solution
#   vector is empty if there is no unique solution.
    

    aug_n = rowReduce(aug)
    if diag_test(aug_n):
        sol = backSub(aug_n)
    else:
        print("\nge_1(): There is no unique solution")
        sol = []
    results = [aug_n, sol]
    return(results)


### The next two functions support checking a solution.

def getAandb(aug):
#   Returns the coef. matrix A and the vector b of Ax=b
    m = rows(aug)
    n = cols(aug)
    A = zero(m,n-1)
    b = zero(m,1)
    for i in range(m):
        for j in range(n-1):
            A[i][j] = aug[i][j]
            
    for i in range(m):
        b[i] = aug[i][n-1]
    Aandb = [A,b]
    return(Aandb)

def checkSol_1(aug,x):
#   For aug=[A|b], returns Ax, b, and b-Ax as vectors
    A  = getAandb(aug)[0]
    b  = getAandb(aug)[1]
    x_col_vec = vec2colVec(x)
    Ax = matMult(A,x_col_vec)
    r  = addVectors(b,scalarMult(-1.0,colVec2vec(Ax)))
    L  = [Ax,b,r]
    return(L)
    
    
#######2 Dimentional Newton ###########
def vec_f(x, y):
    return [[3*x**2-y**2],[3*x*y*y-x*x - 1]]
    
def guess(guess, J, sol):
    dX = backSub(rowReduce( augment(J, colVec2vec(scalarMult(-1, sol))) ))
    return [ [guess[0][0] + dX[0]], [guess[1][0] + dX[1]] ] 
    
def checkE(x):
    check = True;
    for i in range(len(x)):
        if (abs(x[i][0]) > 10**-7):
            check = False;
            break;
    return check;          
       
##### Output 2 Dimentional Newton Method ########
print "\nTwo-Dimentional Newton's Method: \n"   

x = [[1],[1]]
i = 0
          
while (i < 30):
    print "x("+str(i)+") = " + str(x)   
    sol = vec_f(x[0][0], x[1][0])
    print "When X = "+str(x[0][0])+", Y = "+ str(x[1][0])
    print "The solution is: "+ str(sol)
    print
    if ( checkE(sol) ):
        print "\nThe Final Solution: \n"
        print "x = " + str(x[0][0])+"\ny = " + str(x[1][0])
        break;
    else:
        j = [[6*x[0][0], -2*x[1][0]], [3*x[1][0]-2*x[0][0], 3*x[0][0]]]
        x = guess(x, j, sol)
    i+=1 
    
print "\n\nOne-Dimentional Newton's Method\n"
#inital guess
x = 1.0
    
print "Initial Guesse is:" + str(x)
print "\nKeep Guessing: "
while abs(9*x**3-x**2-1) >= 10**(-7):
    x-=(9*x**3-x**2-1)/(27*x**2 - 2*x)
    print x
    
print "\nSo the Final Solution: "
print "x = " +str(x)
print "y = " +str(math.sqrt(3*x*x))
                               
                                                                                           