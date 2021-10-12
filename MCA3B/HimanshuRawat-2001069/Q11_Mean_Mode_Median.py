data = [5, 6, 5, 2, 8, 6, 12, 4]
mean = sum(data) / len(data)
print("mean : ", mean)

median = sorted(data)[len(data) // 2]
print("median : ", median)

mode = max(data, key=data.count)
print("mode : ", mode)
