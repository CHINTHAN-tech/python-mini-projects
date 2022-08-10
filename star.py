def pypart(n):
    mylist = []
    for i in range(1,n+1):
        mylist.append("*"*i)
    print("\n".join(mylist))

n = 5
pypart(n)