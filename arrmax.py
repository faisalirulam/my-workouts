def largest(arr,n):
    max=arr[0]
    for i in range(0,n):
        if(arr[i]>max):
            max=arr[i]
    return max


arr=[]
n = int(input("Enter number of elements : "))
print("Enter the numbers: ")
for i in range(0, n):
	ele = int(input()) 

	arr.append(ele)
ans=largest(arr,n)
print("largest num= ",ans)
