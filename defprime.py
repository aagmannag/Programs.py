def prime(a):
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    if(c==2):
        print("no. is prime")
a=int(input())
prime(a)