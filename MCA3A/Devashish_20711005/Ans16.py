matrix1 = [
    [4, 3],
    [13, 8],
    [10, 2]
]

res = [
    [0, 0, 0],
    [0, 0, 0],
]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        res[j][i] = matrix1[i][j]

for r in res:
    print(r)