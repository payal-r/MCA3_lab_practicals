list = [2,5,4,2,1]

print("Enter an element to be search: ")
elem = int(input())

for i in range(len(list)):
    if elem == list[i]:
        print("\nElement found at Index:", i)
       
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        
print("Sorted List :")
for i in range(len(list)): 
    print(list[i], end="")
