#Write a program to take a input from user and print the fibonacci series to the terminal number:

num = int(input("Enter the terminal number: "))
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(0,num):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3


#output:

#Enter the terminal number: 8
#0 
#1 
#1 
#2 
#3 
#5 
#8 
#13
#21
#34