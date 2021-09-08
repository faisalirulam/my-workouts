t="hello i am tony"
p="tony"
for i in range(len(t)-len(p)):
    for j in range(len(p)):
        while(j<len(p) and p[j]==t[i+1]):
            j=j+1
            
        i=i+1
        if(j==len(p)):
            print(i)
        
        
    