File=open("binaryFile.txt","r")
Data=File.readlines()
print(Data)
for i in Data:
    if i[0] in "joJO":
        print(i,end='')