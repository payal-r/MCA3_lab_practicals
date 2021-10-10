#Write a program to check whether a given number is a prime or not using loop

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

#output:

#Enter the number: 5
#Number is prime