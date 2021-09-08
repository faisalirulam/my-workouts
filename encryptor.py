string="hai"
key=2

newkey=key%26

for i in range(0,len(string)):
    letterposition=string[i]+newkey
    if(letterposition<=122):
        string[i]=letterposition
    else:
        string[i]=(96+letterposition%122)
print(string)


