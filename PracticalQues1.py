import numpy as np
a=[]
b=[]
n=int(input("Enter rows and columns"))
for i in range(n):
    r=[]
    for j in range(n):
        r.append(int(input("number")))
    a.append(r)
print(a)
for i in range(n):
    s=[]
    for j in range(n):
        s.append(int(input("number")))
    b.append(s)
print(b)
c=np.zeros([n,n])
# print(c)
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
print(c)
    

