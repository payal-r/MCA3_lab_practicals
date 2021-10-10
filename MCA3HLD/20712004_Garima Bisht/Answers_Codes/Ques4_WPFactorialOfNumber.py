
print("Enter the Number of which you want to find factorial: ")
num = int(input())

factorial = 1
i = 1
while i<=num:
    factorial = factorial*i
    i = i+1

print("\nFactorial of given number is =", factorial)
