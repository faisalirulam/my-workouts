def magic(n):
    magicSquare = [[0 for x in range(n)]
				for y in range(n)]
    r=1;
    c=(n+1)/2;
    for(i in range(0,(n*n)):

        a[r][c]=i;
        r=r-1
        c=c+1

        if(r<1 && c>n):

        r=r+2;
        c=c-1

        elif(r<1):
        r=n;
        elif(c>n):
        c=1
        elif(a[r][c]!=0):

        r=r+2;
        c=c-1

    for(c in range(1,n)):

    print("\n \t")

    for(c in range(1,n))

    printf(a[r][c])
magic(n)
n=int(input("number="))
