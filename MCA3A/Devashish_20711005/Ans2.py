num=int(input("Enter a number "))
x=0
y=1
sum=0
count=1
while(count<=num):
    x=y
    y=sum
    sum=x+y
    count +=1
    print(sum)
