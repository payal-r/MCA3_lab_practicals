#Write a program to demonstrate the use of nested if statements.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
i = 13
  
if (num1 > num2): 
    if (num1 > num3): 
        print ("Largest no is ", num1) 
    else:
        print("Largest no is ", num3)
else:
    if num2 > num3:
        print("Largest number is ", num2)
    else:
        print("Largest no is ", num3)

#output:

#Enter the first number: 5
#Enter the second number: 4
#Enter the third number: 78
#Largest no is  78