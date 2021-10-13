num=int(input("Enter a number : "))
fact=1
if num<0:
    print("Factorial cannot be determined for negative numbers")
elif num==0:
    print("The Factorial is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
print(fact)
