# f=open("data.txt","w")
# print("file created")
# c=f.write("Hello world")
# # file.close()
# f=open("data.txt","r")
# d=f.read()
# print(d)
# f.close()

# f=open("Story.txt","a")
# f.write("First line of poem")
# f.write("Second line of story")
# f.close()
# print("file close")

# f=open("aa.txt","w")
# f.write("Hello Aagman")
# f.close()

file =open("info.txt","r")
info=file.read()
info.upper()
c=0
for i in range(1,len(info)):
    if('A'<=i and 'Z'>=i):
        c=c+1
    print(c)
