n=int(input("Enter a no."))
sum=0
num=n
while num>0:
    digit=num%10
    sum +=digit**3
    num //=10
if n==sum:
    print(n,"is Armstrong")
else:
    print(n,"is not a Armstrong no.")
