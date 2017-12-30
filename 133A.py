a = str(input())
count = 0
m = 0
for i in range (len(a)):
    if a[i] == 'H' or a[i] == 'Q' or a[i] == '9':
        count += 1
        m = 1 
    else:
        count = 0
if count > 1 or m == 1:
    print ("YES")
else :
    print ("NO")
        
    
    
