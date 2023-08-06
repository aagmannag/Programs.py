File=open("binaryFile.txt","r")
Data=File.read()
for i in Data:
    if i.isdigit():
        print(i,end="")