n = int(input("enter no: "))
flag = 0
for i in range(2, n-1):
  if(n%i==0):
    flag=1
    print("Not a prime number")
    break
if(flag == 0):
  print("Prime number")
