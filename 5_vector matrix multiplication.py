import numpy as np 
def vecMatrixMult():
    r =int(input("Enter length of vector and number of rows in matrix:"))
    c =int(input("Enter number of columns in matrix:"))
    v=[]
    M=[]
    print("Enter Vectors") 
    for i in range(r):
        n=int(input("Enter number:")) 
        v.append(n)
    print("Enter Matrix")
    for i in range(r):
        print("Enter Elements of Rows: ",i+1) 
        M.append([])
        for j in range(c): 
            n=int(input("Enter Number: ")) 
            M[i].append(n)
    print("\nResult of Vector-Matrix multiplication is",np.dot(v,M)) 
def matrixmult():
    M=[]
    N=[]
    r1 =int(input("Enter number of rows in matrix1:"))
    c1 =int(input("Enter number of columns in matrix1:")) 
    print("Enter Matrix1")
    for i in range(r1):
        print("Enter Elements of Rows: ",i+1) 
        M.append([])
    for j in range(c1): 
        n=int(input("Enter Number: ")) 
        M[i].append(n)
    r2 =int(input("Enter number of rows in matrix2:"))
    c2 =int(input("Enter number of columns in matrix2:")) 
    print("Enter Matrix2")
    for i in range(r2):
        print("Enter Elements of Rows: ",i+1) 
        N.append([])
    for j in range(c2): 
        n=int(input("Enter Number: ")) 
        N[i].append(n)
    if(c1 == r2): 
        Mult=np.dot(M,N)
        print("\nResult of Matrix multiplication is") 
    for i in Mult:
        print(i)
while True:
    print("Select Operations")
    print("1. Vector-Matrix Multiplication") 
    print("2. Matrix Multiplication") 
    print("3. Exit")
    ch=int(input("Enter your choice: "))    
    if ch==1:
        vecMatrixMult()
    elif ch==2: 
        matrixmult()
    else:
        break
