def row_echelon(m):
    if not m: 
        return 
    lead= 0
    rowCount = len(m) 
    colCount =len(m[0])
    for r in range(rowCount): 
        if lead>= colCount:
            return 
        i = r
        while m[i][lead] == 0: 
            i+=1
            if i == rowCount:
                i = r
                lead +=1
                if colCount == lead: 
                    return
        m[i],m[r] = m[r],m[i] 
        lv = m[r][lead]
        m[r] = [mrx/float(lv) for mrx in m[r]] 
        for i in range(rowCount):
            if i != r:
                lv=m[i][lead]
                m[i] = [iv - lv*rv for rv,iv in zip(m[r],m[i])] 
        lead+=1
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
print("Enter the matrix: ") 
for row in mtr:
    print(' '.join(("{0:.2f}".format(x) for x in row))) 
row_echelon(mtr)
print("Row Echelon for matrix: ") 
for row in mtr:
    print(' '.join(("{0:.2f}".format(x) for x in row)))
