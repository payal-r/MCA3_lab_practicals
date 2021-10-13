# sorting list 
list = [ 2, 5, 4, 5, 1, 4 ]
sorted_list=sorted(list)
print(sorted_list)



# searching element in a list
mylist = [21, 5, 8, 52, 21, 87, 52]
x = 21

try:

	index = mylist.index(x)
	print('The index of', x, 'in the list is:', index)
except ValueError:
	print('item not present')
