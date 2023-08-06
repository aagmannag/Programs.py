data ="hello world"
r=" "
for c in data:
    if c not in r:
        r=r+c
print(r)