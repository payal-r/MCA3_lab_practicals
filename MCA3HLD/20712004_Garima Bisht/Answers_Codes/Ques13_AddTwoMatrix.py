matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [3, 1, 5],
    [6, 7, 2],
    [8, 4, 9]
]

add = []
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        add.append(matrix1[i][j] + matrix2[i][j])
print(add)

