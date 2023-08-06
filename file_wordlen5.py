File=open("binaryFile.txt","r")
Data=File.read()
Data2=Data.split()
for i in Data2:
    if len(i)==5:
        print(i)
c=0
for i in Data:
    if i==" ":
        c=c+1
print(c)