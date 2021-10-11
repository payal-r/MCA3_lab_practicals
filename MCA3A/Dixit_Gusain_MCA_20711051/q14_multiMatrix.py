X = [[1,5,7],
    [3,5,9],
    [2,4,6]]

Y = [[3,6,9],
    [2,4,6],
    [4,8,12]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)