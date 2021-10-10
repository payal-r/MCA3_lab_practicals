N= int(input("ENTER THE NUMBER :"));
a = 0
b = 1
sum = 0
count = 1
while(count <= N):
    a = b
    b = sum
    sum = a + b
    count += 1
    print(sum)