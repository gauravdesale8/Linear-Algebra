# Practical 8

import numpy as np
print("Enter dimensions of matrix: ") 
r=int(input("Enter the no of rows: ")) 
c=int(input("Enter the no of cols: ")) 
mtr=[]
for i in range (r): 
    mtr.append([])
    print("Enter elements of rows ",i) 
    for j in range(c):
        n=float(input("Enter element: ")) 
        mtr[i].append(n)
print("Entered matrix: ") 
for row in mtr:
    print(' '.join(("{0:.2f}".format(x) for x in row))) 
w, v = np.linalg.eig(mtr)
print("Eigen Values Are:",w) 
print("Eigen Vectors Are:",v)
