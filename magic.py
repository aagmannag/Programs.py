n=int(input("Enter a no."))
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+r
        x=x//10
    x=sum
if sum==1:
    print(n,"is a magic no.")
else:
    print(n,"is not magic no.")