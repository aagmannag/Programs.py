n=int(input("Enter a no."))
for i in range(2,n):
    if n%i==0:
        print(n,"is not prime")
        break
else:
    print(n,"is prime")