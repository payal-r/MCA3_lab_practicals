#Fibonacci series

num=int(input("Enter the last term of fibonacci series :"))
first=0
second=1
while(second <= num):
    print(second )
    temp=first
    first=second
    second=temp+second
