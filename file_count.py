File=open("binaryFile.txt","r")
Data=File.read()
c1=0
c2=0
d=0
print(Data,end="")
for i in Data:
    if(i.islower()):
        c1=c1+1
    if(i.isupper()):
        c2=c2+1
    if(i.isdigit()):
        d=d+1
print("Number of lowercase char is1:",c1)
print("Number of uppercase char is1:",c2)
print("Number of Digits char is1:",d)
