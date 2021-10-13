import statistics
l=[1,2,3,6,8,2,3,2]

#  MEAN

sum=sum(l)
mean=sum/len(l)
print("Mean is", mean)

#  MEDIAN

l.sort()
n=len(l)
if len(l) % 2 == 0:
    median1=l[n//2]
    median2 = l[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = l[n//2]
print("Median is: " + str(median))

#  MODE

mode = statistics.mode(l)
print("Mode of the given list is :", mode)


