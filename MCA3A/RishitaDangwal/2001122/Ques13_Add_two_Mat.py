X = [[1,8,3],
    [4,0,6],
    [7,8,0]]

Y =[[5,2,1],
    [2,3,3],
    [4,5,5]]
add=[]



for i in range(len(X)):
 for j in range(len(X[0])):
       add.append(X[i][j] + Y[i][j])

print(add)