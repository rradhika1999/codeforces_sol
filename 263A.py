l=[]
for i in range (0,5):
    l.append(input().split())  
for i in range (0,5):
    for j in range(0,5):
        if l[i][j]=="1":
            a=i+1
            b=j+1
            break
print (a,b)        
print ((abs(a-3) + abs(b-3)))


    
