factorial = 1
n = int(input("Enter a number: "))
if(n<0):
    print("factorial does not exist for negative numbers")
elif n == 0:
    print("factorial 0 is 1")
else:
    for i in  range(1,n+1):
        factorial = factorial*i
    print("The factorial",n,"is",factorial)