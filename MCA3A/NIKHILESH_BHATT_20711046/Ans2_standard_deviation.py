l = [2,1,4,2,0]
sum=0
for i in range(len(l)):
    sum+=l[i]
mean = sum/len(l)

sumofsqd = 0
for i in range(len(l)):
    sumofsqd+=(l[i]- mean)**2
Standard_Deviation = ((sumofsqd)/len(l))**0.5
print("Standard Deviation is ",Standard_Deviation)
