X = [[1,7,3],
    [4 ,0,6],
    [7 ,0,0]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):

   for j in range(len(Y[0])):
      
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
