n = 5
n0 = 0
n1 = 1
x= 0
if n <= 0:
    print("Enter positive integer")
elif n == 1:
    print("Number in Fibonacci sequence upto",n,":")
    print(n0)
else:
    print("Number in Fibonacci sequence upto",n,":")
    while x < n:
        print(n0,end=", ")
        nth = n0 + n1
        n0 = n1
        n1 = nth
        x += 1    
