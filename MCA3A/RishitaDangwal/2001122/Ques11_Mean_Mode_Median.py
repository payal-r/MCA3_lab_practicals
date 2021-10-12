data = [5, 6, 5, 2, 8, 6, 12, 4]
mean = sum(data)/len(data)
print("MEAN : ",mean)

median = sorted(data) [len(data) // 2]
print("MEDIAN :",median)

mode = max(data, key=data.count)
print("MODE :",mode)