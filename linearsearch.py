def linearsearch(arr):
    for i in range(0,len(arr)):
        if(arr[i]==search):
            print("found at", i+1, "th position")
            break
    else:
        print("not found")
arr=[]
size=int(input("Enter the size:"))
print("The elements are:")
for i in range(0,size):
    element=int(input())
    arr.append(element)
search=int(input("The searching element:"))

linearsearch(arr)

                  
    
    
    
