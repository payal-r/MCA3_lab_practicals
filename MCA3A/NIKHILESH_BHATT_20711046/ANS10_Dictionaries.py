dict1={1:'Graphic',2:'era',3:'University'}
print("Dictionary dict1 is :", dict1)
print("Type of dictionary dict1 is: ",type(dict1))

#To create a dictionary
dict3={}
dict3['a']='name'
dict3['b']='course'
dict3['c']='id'
print("New dictionary dict3 is: ",dict3)

#adding an element to dictionary to dict3

dict3.update({'d':'rollno'})
print("Updated Dictionary dict3 : ",dict3)


print("Keys in dict3: ",dict3.keys())

print("All values in dict3: ",dict3.values())

print("All items in dict3: ",dict3.items())
