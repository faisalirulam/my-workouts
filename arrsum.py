def sum(arr,n):
    sum=0
    for i in range(0,n):
        sum=sum+arr[i]
    return sum


arr=[]
n = int(input("Enter number of elements : "))
print("Enter the numbers: ")
for i in range(0, n):
	ele = int(input()) 

	arr.append(ele)
ans=sum(arr,n)
print("ans= ",ans)
