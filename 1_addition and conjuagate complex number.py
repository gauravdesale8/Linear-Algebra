# Practical 1

import matplotlib.pyplot as plt

S = {3 + 3j, 4 + 3j, 2 + 1j, 2.5 + 1j, 3.25 + 1j}

print("Select Operation:")
print("1: Addition of 2 complex numbers")
print("2: Plot point from set of complex numbers")
print("3: Translation")
print("4: Rotation")
print("5: Scaling")
print("6: Exit")

while True:
    ch = int(input("Enter choice of Operation: "))
    
    if ch == 1:
        c1 = complex(input("Enter Complex number c1: "))
        c2 = complex(input("Enter Complex number c2: "))
        print("Addition of 2 complex numbers:", c1 + c2)
    
    elif ch == 2:
        S1 = {x for x in S}
    
    elif ch == 3:
        c1 = complex(input("Enter translation in complex numbers: "))
        S1 = {x + c1 for x in S}
    
    elif ch == 5:
        scale = float(input("Enter Scale point like (.5) for 1/2: "))
        S1 = {x * scale for x in S}
    
    elif ch == 4:
        angle = int(input("Enter Angle of Rotation: "))
        
        if angle == 90:
            S1 = {x * 1j for x in S}
        elif angle == 180:
            S1 = {x * (-1) for x in S}
        elif angle == 270:
            S1 = {x * 1j * (-1) for x in S}
        else:
            print("Invalid Angle entered")
    
    elif ch == 6:
        break

X = [x.real for x in S1]
Y = [x.imag for x in S1]

plt.plot(X, Y, 'ro')
plt.axis([-6, 6, -6, 6])
plt.show()
