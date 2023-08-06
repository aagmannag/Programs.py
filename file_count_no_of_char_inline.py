File=open("binaryFile.txt","r")
Data=File.readlines()
for i in Data:
    if len(i)>20:
        print(i,end="")