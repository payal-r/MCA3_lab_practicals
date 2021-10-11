# Write a program to find the mean. mode and median of the given range of number.

list1 = [1,2,3,4,5,6,7,8,9,10,2]

sum = 0
for i in list1:
    sum = sum + i

print("-----------------------------------------")
mean = sum /len(list1)
print("Mean of the list is: ",mean)
print()
median =int(len(list1)/2)
print("Meadian of the list is: ",list1[median])
print()
mode = max(set(list1), key = list1.count)
print("Mode of the list is: ",mode)
print("-----------------------------------------")


#output:

#-----------------------------------------
#Mean of the list is:  5.181818181818182  

#Meadian of the list is:  6

#Mode of the list is:  2
#-----------------------------------------