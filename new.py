# b= "aagman"
# print(id(b))
# print(id(b.upper()))
# pi=3.14
# text='the value of pi is '+str(pi)
# print(text)
# print(ord('A'))
# print(chr(65))

# a='first'
# b='last'
# k='a'if a is b else 'a'and 'b'
# out=eval(k)
# print(out,type(out))

# Ist=['a','b','c','d']
# slc=Ist[10:0:-2]
# print(slc)

a=tuple(input().split(" "))
b=tuple(input().split(" "))
c=[]
for i in a:
    for j in b:
        if (i==j):
            c.append(i)
print (tuple(c))

        
