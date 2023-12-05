# Practical 4

global r,c
def printmatrix(A):
    print('the entered matrix M is') 
    for i in range(r):
        print(A[i])
def printrows(A):
    print('Rows of matrix') 
    for i in range (r):
        print('Row%d='%i,A[i])
def printcolumns(A):
    print('columns of matrix') 
    for j in range(c):
        print('column%d='%j,end="")
    for i in range(r):
        print(A[i][j],end="") 
        print('\n')
#Scalar Multiplication 
def scalarmul(A,s):
    N=[[s*A[i][j]
        for j in range(c)] 
            for i in range(r)] 
    print('The scalar multiplication s*M=') 
    printmatrix(N)
#tranpose of matrix M 
def transpose(A):
    T=[[A[i][j] for i in range(r)] for j in range(c)] 
    print('Transpose of M.T=')
    for j in range(c): 
        print(T[j])
#Enter rXc Matrix M
print ('enter the dimensions of matrix ') 
r=int(input('enter no of rows: ')) 
c=int(input('enter no of columns: '))
M=[]
for i in range (r):
    print('enter elements of row',i) 
    M.append([])
    for j in range(c): 
        n=int(input('enter no')) 
        M[i].append(n)
print('Select operation') 
print('1:Display Matrix') 
print('2:Display rows of matrix') 
print('3:Display columns of matrix')
print('4:Scalar Multiplication of matrix') 
print('5:Transpose of matrix')
print('6:Exit')
while True:
    ch=int(input('Enter choice for Operation')) 
    if ch==1:
        printmatrix(M) 
    elif ch==2:
        printrows(M) 
    elif ch==3:
        printcolumns(M) 
    elif ch==4:
        sc=int(input('enter scalar value')) 
        scalarmul(M,sc)
    elif ch==5:
        transpose(M)
    elif ch==6:
        break
