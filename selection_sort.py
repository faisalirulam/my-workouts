x=int(input("Enter the size : "))
A=[]

print("Enter the array : ")
for i in range(0,x):
    elem=int(input())
    A.append(elem)


#A=[89,45,68,90,29,34,17]

for i in range(len(A)):
    min=i
    for j in range(i+1,len(A)):
        if A[min]>A[j]:
            min=j
    A[i],A[min]=A[min],A[i]


print("Sorted array : ")
for i in range(len(A)):
    print(A[i],end=" ")

