n = int(input("Enter the number: "))
print("number before reverse: %d" %n)
reverse=0
while n!=0:
    reverse= reverse*10 + n%10
    n = (n//10)
print("after reverse: %d" %reverse)    