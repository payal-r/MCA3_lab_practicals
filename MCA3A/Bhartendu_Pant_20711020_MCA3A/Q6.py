# Nested if 
n1=21
n2=41
n3=12

if(n1>n2):
    if(n1>n3):
        print(n1, "is greatest number among", n1, n2, n3)
    else:
        print(n3, "is greatest number among", n1, n2, n3)
        
else:
    print(n2, "is greatest number among", n1, n2, n3)
