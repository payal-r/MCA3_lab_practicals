num = int(input("Enter the number: "))
check = False
for i in range(2,num-1):
    if num % i == 0:
        check = True
        break

if check:
    print("Number is not prime")
else:
    print("Number is prime")
