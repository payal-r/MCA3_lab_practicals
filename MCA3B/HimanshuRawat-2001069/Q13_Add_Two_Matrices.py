x = [[1, 3, 2],
     [3, 4, 5],
     [6, 7, 8]]
y = [[8, 7, 6],
     [1, 2, 3],
     [4, 5, 6]]

add = []
for i in range(len(x)):
    for j in range(len(x[0])):
        add.append(x[i][j] + y[i][j])
        print(add)
