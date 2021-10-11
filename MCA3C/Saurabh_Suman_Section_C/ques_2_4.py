#Write a program to calculate the multiplication of two 3x 3 matrices.

num1 = [[15, 4, 13],  
        [12, 14, 16],  
        [4, 17, 9]] 

num2 = [[3, 12, 4],  
        [14, 31, 6],  
        [12, 17, 5]]  

Result = [[0, 0, 0],    
          [0, 0, 0],    
          [0, 0, 0]]  

for m in range(len(num1)):    
   for n in range(len(num2[0])):    
          for o in range(len(num2)):    
               Result[m][n] += num1[m][o] * num2[o][n] 

print("The multiplication result of matrix A and B is: ")  
for res in Result:    
   print(res)


#output:

#The multiplication result of matrix A and B is: 
#[257, 525, 149]
#[424, 850, 212]
#[358, 728, 163]