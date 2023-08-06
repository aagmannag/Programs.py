# lst=['vehicle','object','human','water']
# slc=lst[-1:-1:6]
# print(type(slc))

# lst=[]
# n=int(input("Enter a no. of elements"))
# for i in range(0,n):
#     e=int(input())
#     lst.append(e)
# print(lst)

# n=int(input("Enter a no. of elements :"))
# a=list(map(int,input("Enter the no:").split()))

# out=print('Hello') or print('Python')
# print(out,type(out))

# def prime(x):
#     c=0
#     for i in range(1,x+1):
#         if (x%i==0):
#             c=c+1
#     if c==2:
#         print("prime")
#     else:
#         print("Not prime no")
# a=int(input())
# prime(a)

#class_l={}
# name=input()
# dict={}
# for i in name:
#     dict[i]=dict.get( i ,0)+1
# print(str(dict))

# n=list(map(int,input().split()))
# x=[]
# for i in n:
#     f=n.count(i)
#     x.append(f)
#     a=max(x)
# print("It will require",a,"pockets")

# n=list(map(int,input().split()))
# def myfun(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# even=filter(myfun,n)
# for x in even:
#     print(x)

# f=open('binaryFile.txt','r')
# d=f.readlines()
# for l in d:
#     if l[0]=='A':
#        print(l)
# f.close()

f=open('binaryFile.txt','r')
d=f.readlines()
f.seek(0)
d2=f.read()
d2=d2.replace(" ","")
a=len(d2)
print(a)
for l in d:
    if l[0]is['a','e','i','o','u']:
      print(l)
f.close()