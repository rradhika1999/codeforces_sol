a = input()
b=[]
c=[]
for i in range(len(a)):
    if a[i].isupper():
        b.append(a[i])
    else:
        c.append(a[i])
if len(b)>len(c):
    print(a.upper())
else :
    print(a.lower())
        
