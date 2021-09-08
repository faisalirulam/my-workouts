
# Function to do insertion sort 
def insertionSort(arr): 

	# Traverse through 1 to len(arr) 
	for i in range(1, len(arr)): 

		key = arr[i] 
		j = i-1
		while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
		arr[j+1] = key 


# Driver code to test above
arr=[]
size=int(input("Enter the size:"))
print("Enter the numbers:")
for i in range(0,size):
       element = int(input())
       arr.append(element)
print("The entered elements are:")
print(arr)

insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]) 

