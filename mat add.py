x=int(input("enter the no. of rows of matrix"))
x1=int(input("enter the no of cols of mat"))

print("enter elements 1st mat")
mat1=[[int(input()) for i in range(x)]for i in range(x1)]
for j in mat1:
    print(j)

print("enter 2nd mat")
mat2=[[int(input())for i in range(x)]for i in range(x1)]
for j in mat2:
    print(j)

result=[[0 for i in range(x)]for i in range(x1)]

for i in range(x):
    for j in range(x1):
        result[i][j]=mat1[i][j]+mat2[i][j]

print("sum of mat are")
for i in result:
    print(i)


