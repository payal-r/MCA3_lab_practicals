#Write a program to take a number from user and print its factorial

sum = 1
num = int(input("Enter the number: "))
for i in range(1,num+1):
    sum = sum*i

print("Factorial of a number: ",sum)


#output:

#Enter the number: 6
#Factorial of a number:  720