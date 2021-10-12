n = int(input("Enter a number "))
flag = 0
temp = 0

temp = n/2

while (temp > 0):
    if(n % 2 == 0):
        print("It is not a prime number")
        flag = 1
        break
    if(flag == 0):
        print("It is a prime number")
    break