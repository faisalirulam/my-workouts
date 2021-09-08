num=int(input("Enter a number :"))

copy=num
rev=0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(copy==rev):
    print("num is palindrome")
else:
    print("not palindrome")

string=input("enter a string :")
temp=string
if(string==string[::-1]):
    print("palindrome")
else:
    print("not palindrome")