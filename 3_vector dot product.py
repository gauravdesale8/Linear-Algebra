# Practical 3

def scalarMul(x,p,y,q):
    return sum([(x[i]*p)+(y[i]*q) 
        for i in range (len(x))]) 
def dotMul(x,y):
    return sum([x[i]*y[i] for i in range (len(x))]) 
v=[]
u=[]
n=int(input("Enter the no. of Elements you want to enter in vector: ")) 
print("Enter Elements of vector u: ")
for i in range(n): 
    e=int(input("Enter elements: ")) 
    u.append(e)
print("Vector u = ",u)
print("Enter Elements of vector v: ") 
for i in range(n):
    e=int(input("Enter elements: ")) 
    v.append(e)
print("Vector v = ",v) 
while True:
    print("Select Vector Operation: ") 
    print("1: Scalar Multiplication")
    print("2 : Dot Product")
    print("3: Exit")
    ch=int(input("Enter your Choice: ")) 
    if ch==1:
        print("To perform Scalar Multiplication") 
        a=int(input("Enter the value of a: ")) 
        b=int(input("Enter the value of b: ")) 
        print("Sclar Multiplication =",scalarMul(u,a,v,b))
    elif ch==2:
        print("Dot Product of two matrix is: ",dotMul(u,v)) 
    elif ch==3:
        print("Program Terminated Successfully") 
    break