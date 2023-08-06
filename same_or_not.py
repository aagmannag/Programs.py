a=str(input())
x=a[0]
for i in a:
    if i!=x:
        print("NONE")
        x=i
        break
if x==a[0]:
      print("same")  

