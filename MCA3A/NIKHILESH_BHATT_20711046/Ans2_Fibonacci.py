val=int(input("Enter the number to print fibonacci series"))
a=0
b=1
count=0
if val<=0:
    print("Enter Positive Number")
elif val==1:
        print(a)
else:
    while count < val:
        print(a)
        n=a+b
        a=b
        b=n
        count +=1

