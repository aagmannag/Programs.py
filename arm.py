n=int(input("Enter a no."))
s=n
b=len(str(n))
while n!=0:
    r=n%10
    sum=sum + r**b
    n=n//10
if(sum==s):
    print("arm")
else:
    print("not arm")
