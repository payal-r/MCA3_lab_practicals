#Write a program to calculate the addition of two 3x 3 matrices.
num1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
 
num2= [[11,18,37],
       [61,51,44],
       [13,42,11]]
 
 
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
 
for i in range(len(num1)):  
    for j in range(len(num1[0])):
        result[i][j] = num1[i][j] + num2[i][j]
 
for r in result:
    print(r)


#output:

#[12, 20, 40]
#[65, 56, 50]
#[20, 50, 20]