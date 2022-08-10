from re import I


first,second = 0,1
n= int(input("Enter a number: "))
print("Fibonacci number is: ")
for i in range(0,n):
    if i<=1:
        result=i 
    else:
        result=first+second;
        first=second;
        second=result;
    print(result)        