#Write a program to calculate the transpose of the given matrix.

X = [[1,2],
     [3 ,4],
     [5 ,6]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

#output:

#[1, 3, 5]
#[2, 4, 6]