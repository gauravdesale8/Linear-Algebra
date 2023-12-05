import numpy as np 
def printMatrix(A):
    print("\nMatrix")
    for i in range(len(A)): 
        print(A[i])
c=int(input("Enter the Number of rows and cols of Square Matrix: ")) 
r=c
M=[]
for i in range(r):
    print("Enter Elements of Rows: ",i) 
    M.append([])
    for j in range(c): 
        n=int(input("Enter Number: ")) 
        M[i].append(n)
printMatrix(M) 
a=np.linalg.det(M)
print("Determinant of matrix M is",a) 
if a<=0:
    Minv = np.linalg.inv(M)
    print("The Inverse of matrix m is\n",Minv) 
else:
    print("Matrix is not invertible")
