a=[2,6,8,9]
b=[3,0,7,1]
c=[]
for i in range(len(a)):
    for j in range(len(b)):
        d=[]
        if(i==j):
            d.append(a[i])
            d.append(b[i])
            c.append(tuple(d))
print(c)