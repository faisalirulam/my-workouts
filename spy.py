sum=0
prod=1
num=int(input("Enter a number: "))
while(num>0):
    r=num%10
    sum=sum+r
    prod=prod*r
    num=num//10
if(sum==prod):
    print("The number is spy number")
else:
    print("The num is not a spy number")
