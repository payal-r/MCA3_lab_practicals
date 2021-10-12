tuple=('Welcome','to','MCA')
print("Tuple is :",tuple)
print("length of tuple is: ",len(tuple))

t2=(1,2,3,4)
t3=t2+tuple
print("Tuple after adding different data types tuple is: ",t3)

print("Checking the type of tuple: ", type(t2))

#creating a new tuple by merging value at index 0 from tuple and t2

t5=(' to GEHU','Everyone')
t4=tuple[0]+t5[0]
print("After merging tuple and t5 0th index :",t4)
