l = []
l = input()
if l.isupper():
    print (l.lower())
elif l[1:].isupper():
    print (l[0].upper() + l[1:].lower())
elif len(l) == 1:
    if l.isupper():
        print (l.lower())
    elif l.islower():
         print (l.upper())
else:
    print (l)
        
