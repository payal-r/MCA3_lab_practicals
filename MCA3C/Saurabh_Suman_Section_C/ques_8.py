# Write a program to search the list and sort the list:
def bubble_sort(list1):   
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1



list1 = [2,6,1,9,4,3,8,7,5]
num = int(input("Enter the number you want to search: "))
check = False
count = 0
for i in list1:
    if num == i:
        check = True
        break

if check == True:
    print("number is found")
else:
    print("Number is not found")

print("-----Sorted List----------")
print(bubble_sort(list1))

#output:

#Enter the number you want to search: 5
#number is found
#-----Sorted List---------- 
#[1, 2, 3, 4, 5, 6, 7, 8, 9]