matrix1 = [
    [7, 8, 1],
    [4, 3, 9],
    [9, 1, 8]
]
matrix2 = [
    [4, 2, 3],
    [9, 7, 2],
    [6, 2, 5]
]
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

add = []
for i in range(len(matrix1)):
    for j in range(len(matrix[0])):
        for k in range(len(matrix2)):

            matrix[i][j] += matrix1[i][k] * matrix2[k][j]

for res in matrix:
    print(res)