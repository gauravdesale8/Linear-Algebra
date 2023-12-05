# Practical 2

def scalMul(x, p):
    return [x[i] * p for i in range(len(x))]

def linCom(vlist, clist):
    s = [scalMul(vlist[i], clist[i]) for i in range(len(vlist))]
    l = []
    for j in range(len(s[0])):
        su = 0
        for i in range(len(s)):
            su = su + s[i][j]
        l.append(su)
    return l  # Fix: Corrected the return statement

l = int(input("Enter the length of vector: "))
u = []
v = []
c = []

print("Enter the elements of vector u:")
for i in range(l):
    n = int(input("Enter number: "))
    u.append(n)

print("Enter the elements of vector v:")
for i in range(l):
    n = int(input("Enter number: "))
    v.append(n)

print("Enter the elements of coefficient:")
c1 = int(input("Enter the coefficient of c1: "))
c2 = int(input("Enter the coefficient of c2: "))

newFace = [c1 * u[i] + c2 * v[i] for i in range(len(u))]
print("New Face of u and v:", newFace)

avgFace = [(u[i] + v[i]) / 2 for i in range(len(u))]
print("Average Face of u and v is:", avgFace)
