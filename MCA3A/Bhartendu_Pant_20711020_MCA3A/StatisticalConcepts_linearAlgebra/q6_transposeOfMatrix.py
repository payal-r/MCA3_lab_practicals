# Program to transpose a matrix

X = [[6,3],
    [6 ,3],
    [6 ,3]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
 
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
