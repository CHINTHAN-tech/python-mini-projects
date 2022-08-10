i = 0
result = 0
n=int(input("Enter the number: "))
number1 = n
temp = n
while n!=0:
    n=(n//10)
    i=i+1;
while number1!=0:
    n=number1%10
    result=result+pow(n,i)
    number1=number1//10
if temp==result:
    print("Number is a armstrong")
else:
    print("Not a armstrong number")        