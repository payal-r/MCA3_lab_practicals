X = [[1,4],
    [2 ,5],
    [3 ,6]]

result = [[0,0,0],
         [0,0,0]]


for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

print("Transpose of the matrix is :")
for e in result:
   print(e)
