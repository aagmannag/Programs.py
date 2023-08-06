n=int(input("Enter a no."))
for i in range(n):
    print('  '*i+'* ',end='')
    if i!=(n-1):#except last row
        print('  '*(2*n-2*i-3)+'*',end='')
    print()

