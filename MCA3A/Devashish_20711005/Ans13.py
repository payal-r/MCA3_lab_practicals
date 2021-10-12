matrix1 = [
    [4, 3, 6],
    [1, 5, 8],
    [8, 3, 7]
]
matrix2 = [
    [2, 4, 7],
    [6, 7, 2],
    [8, 2, 9]
]

add = []
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        add.append(matrix1[i][j] + matrix2[i][j])
print(add)