#Write a program to calculate the standard deviation of a given set of numbers.
import math 
list1 = [1,2,3,4,5,6,7,8,9,10,2]
list2=[]

sum = 0
for i in list1:
    sum = sum + i

mean = int(sum /len(list1))

for i in list1:
    diff =abs(int( mean - i))
    list2.append(diff)

sum1 = 0
for i in list2:
    sum1 = sum1 +(i*i)
    
sum1 = sum1/len(list2)
std = math.sqrt(sum1)


print("Standard deviation is: ",std)

#output:

#Standard deviation is:  2.9232609437842774