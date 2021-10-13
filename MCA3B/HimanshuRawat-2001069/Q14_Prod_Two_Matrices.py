x = [[1, 3, 2],
     [3, 4, 5],
     [6, 7, 8]]
y = [[8, 7, 6],
     [1, 2, 3],
     [4, 5, 6]]

prod = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            prod[i][j] += x[i][k] * y[k][j]
    for r in prod:
        print(r)
