n = int(input("Enter a number: "))
rev = 0
temp = n
while(n>0):
    dig = n%10
    rev = rev*10+dig
    n = n//10
if(temp==rev):
    print("The number is palindrome")
else:
    print("The number is not palindrome")