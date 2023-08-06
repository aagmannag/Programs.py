n=int(input("Enter a no."))
def reverse(n):
    r=0
    while(n!=0):
        d=n%10
        r=r*10+d
        n=n//10
    print(r)
out=reverse(n)
