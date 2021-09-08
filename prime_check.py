def prime_check(value):
    flag=0
    if(value > 1):
        for i in range(2,value):
            if(value%i==0):
                flag=1
                break
    if flag:
        print("not prime")
    else:
        print("prime")
                
        



value=4
prime_check(value)