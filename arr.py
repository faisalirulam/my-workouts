# creating an empty list 
lst = []

# number of elemetns as input 
n = int(input("Enter number of elements : "))
print("Enter the numbers: ")
# iterating till the range 
for i in range(0, n):
	ele = int(input()) 

	lst.append(ele) # adding the element 
	
print(lst) 
