n=int(input("Enter a no."))
s=0
num=n
while(n>0):
    digit=n%10
    fact=1
    for i in range (1,digit+1):
        fact=fact*i
    s=s+fact
    n=n//10
if(s==num):
    print("Strong no.")
else:
    print("not a strong no.")