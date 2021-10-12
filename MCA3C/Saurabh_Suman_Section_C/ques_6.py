#Write a program to demostrate the importing of modules of python
import modules
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
num = modules.add(a,b)
print("Sum of a number: ",num)

num1 = modules.mul(a,b)
print("Multiplication of a number: ",num1)

num2 = modules.sub(a,b)
print("Substraction of a two number: ",num2)

#output:

#Enter the first number: 5
#Enter the second number: 14 
#Sum of a number:  19
#Multiplication of a number:  70  
#Substraction of a two number:  -9