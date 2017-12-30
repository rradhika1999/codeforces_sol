a = (input())
n=list(map(int, a))
for i in range(len(a)-1):
    if n[i] == n[i+1]:
        (a) = (str((int)(a)+1))
print (a)       
