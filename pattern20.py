n=int(input("Enter a no."))
for i in range(n):
    print('  '*i+chr(65+i)+' ',end='')
    if i!=n-1:
        print('  '*(2*n-2*i-3)+chr(65+i),end='')
    print()